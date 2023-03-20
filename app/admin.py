from django.contrib import admin
from .models import *


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'games', 'wins', 'rating')