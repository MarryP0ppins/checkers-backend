from datetime import datetime
from datetime import timedelta

import jwt
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from time import time

from .managers import UserManager

import os


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(db_index=True, max_length=16, unique=True)
    email = models.EmailField(db_index=True, unique=True, max_length=32)

    is_staff = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Свойство USERNAME_FIELD сообщает нам, какое поле мы будем использовать
    # для входа в систему. В данном случае мы хотим использовать почту.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.username

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token, вместо
        user._generate_jwt_token(). Декоратор @property выше делает это
        возможным. token называется "динамическим свойством".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return self.username

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.username

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        print(time() + 8640000)
        token = jwt.encode({
            'id': self.pk,
            'exp': time() + 8640000
        }, os.getenv('SECRET_KEY'), algorithm='HS256')
        return token
