from rest_framework import status, filters
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from app.permissions import IsSuperUser
from app.serializers import *
from authentication.serializers import *
from app.utils import create_moves_json


class ProfileViewSet(GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    ordering_fields = ['games', 'rating', 'wins', 'username']
    ordering = ['-rating', '-wins', 'games', 'username']
    search_fields = ['user__username']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.filter_queryset(self.queryset), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Profile.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None, **kwargs):
        try:
            user_info = Profile.objects.get(pk=pk)
        except user_info.DoesNotExist:
            return Response(
                {'message': 'Данного пользователя не существует'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(
            user_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameViewSet(GenericViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['status']
    search_fields = ['user_1__username', 'user_2__username']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.filter_queryset(self.queryset), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Game.objects.all()
        games = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(games)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None, **kwargs):
        try:
            game = Game.objects.get(pk=pk)
        except game.DoesNotExist:
            return Response(
                {'message': 'Данной игры не существует'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(
            game, data=request.data, partial=True)
        if serializer.is_valid():
            if serializer.validated_data.get('status') == 'FINISHED':
                moves = Move.objects.filter(game=pk)
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
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, **kwargs):
        game = Game.objects.get(pk=pk)
        moves = Move.objects.filter(game=pk)
        if moves:
            moves.delete()
        if game:
            game.delete()
            return Response({"status": "ok"}, status=status.HTTP_200_OK)
        return Response({"status": "error"},
                        status=status.HTTP_400_BAD_REQUEST)


class MoveViewSet(GenericViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game', 'user', 'checker_id', 'is_last_move']
    ordering = ['id']
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        last_move = Move.objects.filter(game_id=request.data.get(
            'game'), checker_id=request.data.get('checker_id')).last()
        if last_move:
            last_move.is_last_move = False
            last_move.save()
        if request.data.get('killed'):
            killed = request.data.pop('killed')
            Move.objects.filter(game=request.data.get(
                'game'), checker_id__in=killed).update(is_dead=True)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        game = Game.objects.get(pk=serializer.data.get('game'))
        game.user_1_turn = not game.user_1_turn
        game.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.filter_queryset(self.queryset), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Move.objects.all()
        games = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(games)
        return Response(serializer.data, status=status.HTTP_200_OK)
