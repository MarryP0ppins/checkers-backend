from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from .permissions import IsSuperUser
from app.serializers import *
from authentication.serializers import *


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
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


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    search_fields = ['username_1', 'username_2']
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.filter_queryset(self.queryset), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Games.objects.all()
        games = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(games)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None, **kwargs):
        try:
            games = Games.objects.get(pk=pk)
        except games.DoesNotExist:
            return Response(
                {'message': 'The games info does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(
            games, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, **kwargs):
        game = Games.objects.get(pk=pk)
        if game:
            game.delete()
            return Response({"status": "ok"}, status=status.HTTP_200_OK)
        return Response({"status": "error"},
                        status=status.HTTP_400_BAD_REQUEST)
