from rest_framework import serializers
from app.models import Game, Move
from app.utils import create_moves_json
from authentication.models import User
from authentication.serializers import UserSerializer
from grpc_server.grpc.grpc_server_pb2 import GameResponse, MoveResponse
from datetime import datetime


class CreateGameProtoSerializer(serializers.ModelSerializer):
    user_1 = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)
    user_2 = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)
    user_1_info = UserSerializer(read_only=True)
    user_2_info = UserSerializer(read_only=True)
    user_1_points = serializers.DecimalField(
        max_digits=4, decimal_places=2, coerce_to_string=False, required=False)
    user_2_points = serializers.DecimalField(
        max_digits=4, decimal_places=2, coerce_to_string=False, required=False)
    moves = serializers.DictField(child=serializers.ListField(child=serializers.ListField(
        child=serializers.CharField(max_length=2))), read_only=True, required=False)
    start_at = serializers.CharField(read_only=True)
    finish_at = serializers.CharField(read_only=True)
    user_1_turn = serializers.BooleanField(read_only=True, required=False)
    status = serializers.CharField(max_length=64, required=False)

    class Meta:
        model = Game
        proto_class = GameResponse
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

    def update(self, instance, validated_data):
        instance.winner = validated_data.get('winner', instance.winner)
        instance.user_1_points = validated_data.get(
            'user_1_points', instance.user_1_points)
        instance.user_2_points = validated_data.get(
            'user_2_points', instance.user_2_points)
        instance.status = validated_data.get('status', instance.status)

        user_1 = User.objects.get(pk=instance.user_1.id)
        user_2 = User.objects.get(pk=instance.user_2.id)
        moves = Move.objects.filter(game=instance.id)
        
        if moves:
            instance.moves = create_moves_json(
                moves, user_1.username, user_2.username)
            moves.delete()

        return {
            "id": instance.id,
            "user_1_turn": instance.user_1_turn,
            "user_1_info": UserSerializer(user_1).data,
            "user_2_info": UserSerializer(user_2).data,
            "winner": instance.winner,
            "user_1_points": instance.user_1_points,
            "user_2_points": instance.user_2_points,
            "start_at": instance.start_at,
            "finish_at": datetime.now(),
            "status": instance.status
        }


class CreateMoveProtoSerializer(serializers.ModelSerializer):
    is_last_move = serializers.BooleanField(read_only=True)
    new_positions = serializers.ListField(
        child=serializers.CharField(max_length=2))
    is_dead = serializers.BooleanField(read_only=True)

    class Meta:
        model = Move
        proto_class = MoveResponse
        fields = ["id", "game", "user", "checker_id", "new_positions",
                  "is_white", "is_king", "is_dead", "is_last_move"]

    # def create(self, validated_data):
    #     game = Move.objects.create(**validated_data)
    #     print(game.new_positions)
    #     return game
