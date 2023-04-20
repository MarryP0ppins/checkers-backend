from rest_framework import serializers
from app.models import *


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('_get_username')

    def _get_username(self, data):
        return f'{data.user.username}'

    class Meta:
        model = Profile

        fields = ["id", "username", "wins", "games", "rating"]


class GameSerializer(serializers.ModelSerializer):

    """user_1 = serializers.SerializerMethodField('_get_username_1')
    user_2 = serializers.SerializerMethodField('_get_username_2')

    def _get_username_1(self, data):
        return f'{data.user_1.username}'

    def _get_username_2(self, data):
        return f'{data.user_2.username}'"""

    class Meta:
        model = Game

        fields = [
            "id",
            "user_1",
            "user_2",
            "user_1_turn",
            "start_at",
            "finish_at",
            "status",
            "moves"]


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move

        fields = ["id", "game", "user", "checker_id",
                  "new_positions", "is_last_move", "is_white", "is_king"]
