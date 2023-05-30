from django_socio_grpc import generics
from app.models import Game, Move, Profile
from app.utils import create_moves_json
from .serializers import CreateGameProtoSerializer, CreateMoveProtoSerializer
from grpc_server.grpc.grpc_server_pb2 import GameResponse, MoveResponse
from asgiref.sync import sync_to_async
from rest_framework import status


class GameService(generics.ModelService):
    queryset = Game.objects.all()
    serializer_class = CreateGameProtoSerializer

    def Create(self, request, context):

        print(request)
        serializer = self.serializer_class(data={
            "user_1": request.user_1,
            "user_2": request.user_2
        })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
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
            "user_1_points": request.user_1_points,
            "user_2_points": request.user_2_points,
            "status": request.status
        }, partial=True)
        if serializer.is_valid():
            if serializer.validated_data.get('status') == 'FINISHED':
                moves = Move.objects.filter(game=request.id)
                if moves:
                    game.moves = create_moves_json(moves)
                    moves.delete()
                profile_1 = Profile.objects.get(user__id=game.user_1_id)
                profile_2 = Profile.objects.get(user__id=game.user_2_id)
                if profile_1:
                    profile_1.rating = profile_1.rating + \
                        serializer.validated_data.get('user_1_points')
                    profile_1.games = profile_1.games + 1
                    if serializer.validated_data.get('winner') == 'USER_1':
                        profile_1.wins = profile_1.wins + 1
                if profile_2:
                    profile_2.rating = profile_2.rating + \
                        serializer.validated_data.get('user_2_points')
                    profile_2.games = profile_2.games + 1
                    if not serializer.validated_data.get('winner') == 'USER_2':
                        profile_1.wins = profile_1.wins + 1
            serializer.save()
            return GameResponse(**serializer.data)
        return Exception(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoveService(generics.AsyncModelService):
    queryset = Move.objects.all()
    serializer_class = CreateMoveProtoSerializer

    def Create(self, request, context):

        print(type(request.new_positions))
        new_positions = [_ for _ in request.new_positions]
        killed = [_ for _ in request.killed]
        last_move = Move.objects.filter(
            game_id=request.game, checker_id=request.checker_id).last()
        if last_move:
            last_move.is_last_move = False
            last_move.save()
        if killed:
            Move.objects.filter(
                game=request.game, checker_id__in=killed).update(is_dead=True)
        serializer = self.serializer_class(data={
            "game": request.game,
            "user": request.user,
            "checker_id": request.checker_id,
            "new_positions": new_positions,
            "is_king": request.is_king,
            "is_white": request.is_white,
            "is_dead": request.is_dead
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        game = Game.objects.get(pk=serializer.data.get('game'))
        game.user_1_turn = not game.user_1_turn
        game.save()
        print(serializer.data)
        return MoveResponse(**serializer.data)
