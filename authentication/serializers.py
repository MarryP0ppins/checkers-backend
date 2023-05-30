from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from app.models import Profile
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username"]


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Creates a new user.
    Email, username, and password are required.
    Returns a JSON web token.
    """

    # The password must be validated and should not be read by the client
    password = serializers.CharField(
        max_length=16,
        min_length=4,
        write_only=True,
    )
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password2')

    def create(self, validated_data):
        password = validated_data["password"]
        password2 = validated_data.pop("password2")

        if password != password2:
            raise serializers.ValidationError('Пароли не совпадают')

        user = User.objects.create_user(**validated_data)
        profile = Profile.objects.create(user=user)
        profile.save()

        return user


class LoginSerializer(serializers.Serializer):
    # Authenticates an existing user.
    # Email and password are required.
    # Returns a JSON web token.

    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    # Ignore these fields if they are included in the request.
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data) -> User:
        # Validates user data.

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Пользователя с такой почтой не существует'
            )

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Пользователя с такой почтой или паролем не существует'
            )

        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        update_last_login(None, user)

        validation = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'access': access_token,
            'refresh': refresh_token,
        }

        return validation


class UserRetrieveUpdateSerializer(serializers.ModelSerializer):
    """ Осуществляет сериализацию и десериализацию объектов User. """

    # Пароль должен содержать от 8 до 128 символов. Это стандартное правило. Мы
    # могли бы переопределить это по-своему, но это создаст лишнюю работу для
    # нас, не добавляя реальных преимуществ, потому оставим все как есть.
    password = serializers.CharField(
        max_length=16,
        min_length=8,
        write_only=True
    )

    profile = serializers.SerializerMethodField('_get_profile')

    def _get_profile(self, user):
        profile = Profile.objects.get(pk=user.id)
        return {
            "wins": profile.wins,
            "games": profile.games,
            "rating": profile.rating,
        }

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'profile')

        # Параметр read_only_fields является альтернативой явному указанию поля
        # с помощью read_only = True, как мы это делали для пароля выше.
        # Причина, по которой мы хотим использовать здесь 'read_only_fields'
        # состоит в том, что нам не нужно ничего указывать о поле. В поле
        # пароля требуются свойства min_length и max_length,
        # но это не относится к полю токена.
        # read_only_fields = ('id')

    def update(self, instance, validated_data):
        # Выполняет обновление User.

        # В отличие от других полей, пароли не следует обрабатывать с помощью
        # setattr. Django предоставляет функцию, которая обрабатывает пароли
        # хешированием и 'солением'. Это означает, что нам нужно удалить поле
        # пароля из словаря 'validated_data' перед его использованием далее.
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            # Для ключей, оставшихся в validated_data мы устанавливаем значения
            # в текущий экземпляр User по одному.
            setattr(instance, key, value)

        if password is not None:
            # 'set_password()' решает все вопросы, связанные с безопасностью
            # при обновлении пароля, потому нам не нужно беспокоиться об этом.
            instance.set_password(password)

        # После того как все было обновлено, мы должны сохранить наш экземпляр
        # User. Стоит отметить, что set_password() не сохраняет модель.
        instance.save()

        return instance


class CustomTokenRefreshSerializer(TokenRefreshSerializer):

    # Ignore these fields if they are included in the request.
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255)

    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)
        user_uid = decoded_payload['user_id']
        user = User.objects.get(pk=user_uid)
        # add filter query
        data.update({'id': user_uid, 'username': user.username, 'email': user.email})
        return data
