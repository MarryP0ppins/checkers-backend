from django.contrib import admin
from app.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'games', 'wins', 'rating')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_1',
        'user_2',
        'start_at',
        'finish_at',
        'status')


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'user', 'checker_id', 'is_white')
