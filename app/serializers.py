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
    userOne = serializers.IntegerField(write_only=True)
    userTwo = serializers.IntegerField(write_only=True)
    userOneInfo = serializers.SerializerMethodField(
        '_get_user_1', read_only=True)
    userTwoInfo = serializers.SerializerMethodField(
        '_get_user_2', read_only=True)
    moves = serializers.DictField(child=serializers.ListField(
        child=serializers.CharField(max_length=2)), read_only=True)
    startAt = serializers.DateTimeField(read_only=True)
    finishAt = serializers.DateTimeField(read_only=True)
    userOneTurn = serializers.BooleanField(read_only=True)

    def _get_user_1(self, data):
        return {
            'id': data.userOne.id,
            'username': data.userOne.username
        }

    def _get_user_2(self, data):
        return {
            'id': data.userTwo.id,
            'username': data.userTwo.username
        }

    class Meta:
        model = Game
        fields = ["id",
                  "userOne",
                  "userTwo",
                  "userOneInfo",
                  "userTwoInfo",
                  "userOneTurn",
                  "winner",
                  "userOnePoints",
                  "userTwoPoints",
                  "startAt",
                  "finishAt",
                  "status",
                  "moves"]


class MoveSerializer(serializers.ModelSerializer):
    isLastMove = serializers.BooleanField(read_only=True)
    newPositions = serializers.ListField(
        child=serializers.CharField(max_length=2))
    isDead = serializers.BooleanField(read_only=True)

    class Meta:
        model = Move
        fields = ["id", "game", "user", "checkerId", "newPositions",
                  "isWhite", "isKing", "isDead", "isLastMove"]
