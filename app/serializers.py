from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('_get_username')

    def _get_username(self, user):
        return f'{user.user.username}'

    class Meta:
        model = Profile

        fields = ["id", "username", "wins", "games", "rating"]


class GamesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Games

        fields = [
            "id",
            "username_1",
            "username_2",
            "start_at",
            "finish_at",
            "moves"]
