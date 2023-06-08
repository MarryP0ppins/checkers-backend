from app.models import *
from grpc_server.serializers import CreateGameProtoSerializer, CreateMoveProtoSerializer
from grpc_server.grpc.grpc_server_pb2_grpc import GameControllerServicer, add_GameControllerServicer_to_server, MoveControllerServicer, add_MoveControllerServicer_to_server
from grpc_server.grpc.grpc_server_pb2 import GameResponse, MoveResponse
from rest_framework import status


def grpc_hook(server):
    add_GameControllerServicer_to_server(GameController(), server)
    add_MoveControllerServicer_to_server(MoveController(), server)


class GameController(GameControllerServicer):
    queryset = Game.objects.all()
    serializer_class = CreateGameProtoSerializer

    def Create(self, request, context):
        serializer = self.serializer_class(data={
            "userOne": request.userOne,
            "userTwo": request.userTwo
        })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return GameResponse(**serializer.data)
        return Exception('game_create_error')

    def PartialUpdate(self, request, context):
        try:
            game = Game.objects.get(pk=request.id)
        except game.DoesNotExist:
            return Exception(
                {'message': 'Данной игры не существует'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(game, data={
            "winner": request.winner,
            "userOnePoints": request.userOnePoints,
            "userTwoPoints": request.userTwoPoints,
            "status": request.status
        }, partial=True)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data.get('status') == 'FINISHED':
                profile_1 = Profile.objects.get(user__id=game.userOne_id)
                profile_2 = Profile.objects.get(user__id=game.userTwo_id)
                if profile_1:
                    profile_1.rating = profile_1.rating + \
                        serializer.validated_data.get('userOnePoints')
                    profile_1.games = profile_1.games + 1
                    if serializer.validated_data.get('winner') == 'USER_1':
                        profile_1.wins = profile_1.wins + 1
                if profile_2:
                    profile_2.rating = profile_2.rating + \
                        serializer.validated_data.get('userTwoPoints')
                    profile_2.games = profile_2.games + 1
                    if not serializer.validated_data.get('winner') == 'USER_2':
                        profile_1.wins = profile_1.wins + 1
            serializer.save()
            return GameResponse(**serializer.data)
        return Exception(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoveController(MoveControllerServicer):
    queryset = Move.objects.all()
    serializer_class = CreateMoveProtoSerializer

    def Create(self, request, context):
        new_positions = [_ for _ in request.newPositions]
        killed = [_ for _ in request.killed]
        last_move = Move.objects.filter(
            game_id=request.game, checkerId=request.checkerId).last()
        if last_move:
            last_move.isLastMove = False
            last_move.save()
        if killed:
            Move.objects.filter(
                game=request.game, checkerId__in=killed).update(isDead=True)
        serializer = self.serializer_class(data={
            "game": request.game,
            "user": request.user,
            "checkerId": request.checkerId,
            "newPositions": new_positions,
            "isKing": request.isKing,
            "isWhite": request.isWhite,
            "isDead": request.isDead
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        game = Game.objects.get(pk=serializer.data.get('game'))
        game.userOneTurn = not game.userOneTurn
        game.save()
        return MoveResponse(**serializer.data)
