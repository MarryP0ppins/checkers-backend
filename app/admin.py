from django.contrib import admin
from .models import *


@admin.register(Profile)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'games', 'wins', 'rating')


@admin.register(Games)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username_1', 'username_2', 'start_at', 'finish_at')
