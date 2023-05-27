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
    user_1 = serializers.IntegerField(write_only=True)
    user_2 = serializers.IntegerField(write_only=True)
    user_1_info = serializers.SerializerMethodField(
        '_get_user_1', read_only=True)
    user_2_info = serializers.SerializerMethodField(
        '_get_user_2', read_only=True)
    moves = serializers.DictField(child=serializers.ListField(
        child=serializers.CharField(max_length=2)), read_only=True)
    start_at = serializers.DateTimeField(read_only=True)
    start_at = serializers.DateTimeField(read_only=True)
    user_1_turn = serializers.BooleanField(read_only=True)
    def _get_user_1(self, data):
        return {
            'id': data.user_1.id,
            'username': data.user_1.username
        }

    def _get_user_2(self, data):
        return {
            'id': data.user_2.id,
            'username': data.user_2.username
        }

    class Meta:
        model = Game

        fields = [
            "id",
            "user_1",
            "user_2",
            "user_1_info",
            "user_2_info",
            "user_1_turn",
            "winner",
            "user_1_points",
            "user_2_points",
            "start_at",
            "finish_at",
            "status",
            "moves"]


class MoveSerializer(serializers.ModelSerializer):
    is_last_move = serializers.BooleanField(read_only=True)
    new_positions = serializers.ListField(
        child=serializers.CharField(max_length=2))
    is_dead=serializers.BooleanField(read_only=True)

    class Meta:
        model = Move

        fields = ["id", "game", "user", "checker_id", "new_positions",
                  "is_white", "is_king", "is_dead", "is_last_move"]
