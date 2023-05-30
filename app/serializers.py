from typing import Dict
from rest_framework import serializers
from app.models import *
from authentication.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('_get_username')

    def _get_username(self, data):
        return f'{data.user.username}'

    class Meta:
        model = Profile

        fields = ["id", "username", "wins", "games", "rating"]


class GameSerializer(serializers.ModelSerializer):
    user_1 = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)
    user_2 = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)
    user_1_info = UserSerializer(read_only=True)
    user_2_info = UserSerializer(read_only=True)
    moves = serializers.DictField(child=serializers.ListField(child=serializers.ListField(
        child=serializers.CharField(max_length=2))), read_only=True, required=False)
    start_at = serializers.CharField(read_only=True)
    finish_at = serializers.CharField(read_only=True)
    user_1_turn = serializers.BooleanField(read_only=True, required=False)
    status = serializers.CharField(max_length=64, required=False)

    class Meta:
        model = Game
        fields = ["id",
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

    def create(self, validated_data):
        game = Game.objects.create(**validated_data)
        user_1 = User.objects.get(pk=game.user_1.id)
        user_2 = User.objects.get(pk=game.user_2.id)
        # .strftime("%Y-%m-%d %H:%M:%S")
        return {
            "id": game.id,
            "user_1_turn": game.user_1_turn,
            "user_1_info": UserSerializer(user_1).data,
            "user_2_info": UserSerializer(user_2).data,
            "start_at": game.start_at,
            "status": game.status
        }


class MoveSerializer(serializers.ModelSerializer):
    is_last_move = serializers.BooleanField(read_only=True)
    new_positions = serializers.ListField(
        child=serializers.CharField(max_length=2))
    is_dead = serializers.BooleanField(read_only=True)

    class Meta:
        model = Move
        fields = ["id", "game", "user", "checker_id", "new_positions",
                  "is_white", "is_king", "is_dead", "is_last_move"]
