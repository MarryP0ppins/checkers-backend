from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .permissions import IsSuperUser
from app.serializers import *


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    ordering_fields = ['games', 'rating', 'wins']
    ordering = ['-rating', '-wins', 'games']
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'partial_update']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsSuperUser]
        return [permission() for permission in permission_classes]
    
    def list(self, request, *args, **kwargs):
        serializer = UserInfoSerializer(self.filter_queryset(self.queryset), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = UserInfo.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = UserInfoSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None, **kwargs):
        try:
            user_info = UserInfo.objects.get(pk=pk)
        except user_info.DoesNotExist:
            return Response({'message': 'The user info does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserInfoSerializer(user_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    