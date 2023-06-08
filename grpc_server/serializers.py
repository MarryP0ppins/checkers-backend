from rest_framework import serializers
from app.models import Game, Move
from app.utils import create_moves_json
from authentication.models import User
from authentication.serializers import UserSerializer
from grpc_server.grpc.grpc_server_pb2 import GameResponse, MoveResponse
from datetime import datetime


class CreateGameProtoSerializer(serializers.ModelSerializer):
    userOne = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)
    userTwo = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)
    userOneInfo = UserSerializer(read_only=True)
    userTwoInfo = UserSerializer(read_only=True)
    userOnePoints = serializers.DecimalField(
        max_digits=4, decimal_places=2, coerce_to_string=False, required=False)
    userTwoPoints = serializers.DecimalField(
        max_digits=4, decimal_places=2, coerce_to_string=False, required=False)
    moves = serializers.DictField(child=serializers.ListField(child=serializers.ListField(
        child=serializers.CharField(max_length=2))), read_only=True, required=False)
    startAt = serializers.CharField(read_only=True)
    finishAt = serializers.CharField(read_only=True)
    userOneTurn = serializers.BooleanField(read_only=True, required=False)
    status = serializers.CharField(max_length=64, required=False)

    class Meta:
        model = Game
        proto_class = GameResponse
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

    def create(self, validated_data):
        game = Game.objects.create(**validated_data)
        user_1 = User.objects.get(pk=game.userOne.id)
        user_2 = User.objects.get(pk=game.userTwo.id)
        # .strftime("%Y-%m-%d %H:%M:%S")
        return {
            "id": game.id,
            "userOneTurn": game.userOneTurn,
            "userOneInfo": UserSerializer(user_1).data,
            "userTwoInfo": UserSerializer(user_2).data,
            "startAt": game.startAt,
            "status": game.status
        }

    def update(self, instance, validated_data):
        instance.winner = validated_data.get('winner', instance.winner)
        instance.userOnePoints = validated_data.get(
            'user_1_points', instance.userOnePoints)
        instance.userTwoPoints = validated_data.get(
            'user_2_points', instance.userTwoPoints)
        instance.status = validated_data.get('status', instance.status)

        user_1 = User.objects.get(pk=instance.userOne.id)
        user_2 = User.objects.get(pk=instance.userTwo.id)
        moves = Move.objects.filter(game=instance.id)
        
        if moves:
            instance.moves = create_moves_json(
                moves, user_1.username, user_2.username)
            moves.delete()

        return {
            "id": instance.id,
            "userOneTurn": instance.userOneTurn,
            "userOneInfo": UserSerializer(user_1).data,
            "userTwoInfo": UserSerializer(user_2).data,
            "winner": instance.winner,
            "userOnePoints": instance.userOnePoints,
            "userTwoPoints": instance.userTwoPoints,
            "startAt": instance.startAt,
            "finishAt": datetime.now(),
            "status": instance.status
        }


class CreateMoveProtoSerializer(serializers.ModelSerializer):
    isLastMove = serializers.BooleanField(read_only=True)
    newPositions = serializers.ListField(
        child=serializers.CharField(max_length=2))
    isDead = serializers.BooleanField(read_only=True)

    class Meta:
        model = Move
        proto_class = MoveResponse
        fields = ["id", "game", "user", "checkerId", "newPositions",
                  "isWhite", "isKing", "isDead", "isLastMove"]