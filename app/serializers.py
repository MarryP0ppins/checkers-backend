from rest_framework import serializers
from .models import *
from authentication.models import User


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('_get_username')
    
    def _get_username(self, user):
        return f'{user.user.username}'
        
        
    class Meta:
        model = Profile
        
        fields = ["id", "username", "wins", "games", "rating"]
