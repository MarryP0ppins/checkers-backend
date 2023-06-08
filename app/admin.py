from django.contrib import admin
from app.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'games', 'wins', 'rating')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'userOne',
        'userTwo',
        'startAt',
        'finishAt',
        'status')


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'user', 'checkerId', 'isWhite')
