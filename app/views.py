from rest_framework import status, filters
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from app.permissions import IsSuperUser
from app.serializers import *
from authentication.serializers import *
from app.utils import create_moves_json, create_start_moves


class ProfileViewSet(GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['games', 'rating', 'wins']
    ordering = ['-rating', '-wins', 'games']
    search_fields = ['user__username']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'partial_update']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsSuperUser]
        return [permission() for permission in permission_classes]

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
                {'message': 'The user info does not exist'}, status=status.HTTP_404_NOT_FOUND)
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
    search_fields = ['username_1', 'username_2']
    permission_classes = [IsAuthenticatedOrReadOnly]
    #permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Move.objects.bulk_create(
            create_start_moves(
                Game.objects.get(pk=serializer.data.get('id')),
                User.objects.get(pk=serializer.data.get('user_1')),
                User.objects.get(pk=serializer.data.get('user_2'))
            ))
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
            games = Game.objects.get(pk=pk)
        except games.DoesNotExist:
            return Response(
                {'message': 'The games info does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(
            games, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, **kwargs):
        game = Game.objects.get(pk=pk)
        if game:
            game.delete()
            return Response({"status": "ok"}, status=status.HTTP_200_OK)
        return Response({"status": "error"},
                        status=status.HTTP_400_BAD_REQUEST)


class MoveViewSet(GenericViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game', 'user', 'checker_id']
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        game = Game.objects.get(pk=serializer.data.get('game_id'))
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

    def destroy(self, request, pk=None, **kwargs):
        moves = Move.objects.filter(game=pk)
        if moves:
            game = Game.objects.get(pk=pk)
            game.moves = create_moves_json(moves)
            game.save()
            moves.delete()
            return Response({"status": "ok"}, status=status.HTTP_200_OK)
        return Response({"status": "error"},
                        status=status.HTTP_400_BAD_REQUEST)
