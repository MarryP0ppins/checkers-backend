from rest_framework import serializers
from .models import *



class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        
        fields = ["id", "wins", "games", "rating"]
