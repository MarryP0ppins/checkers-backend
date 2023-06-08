from django.db import models
from django.utils.translation import gettext_lazy as _
from authentication.models import User


def get_unknown_user():
    return User.objects.get_or_create(
        username='unknown',
        password='unknown',
        email='unknown@unknown.unknown',
        is_staff=False)[0]


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    rating = models.PositiveSmallIntegerField(default=0)


class Game(models.Model):
    class GameStatus(models.TextChoices):
        CREATED = 'CREATED'
        IN_PROCESS = 'IN_PROCESS'
        FINISHED = 'FINISHED'

    class WinnerStatus(models.TextChoices):
        USER_1 = 'USER_1'
        USER_2 = 'USER_2'
        DRAW = 'DRAW'

    id = models.BigAutoField(primary_key=True)
    userOne = models.ForeignKey(
        User, on_delete=models.SET(get_unknown_user), related_name='user_1')
    userTwo = models.ForeignKey(
        User, on_delete=models.SET(get_unknown_user), related_name='user_2')
    userOneTurn = models.BooleanField(default=True)
    winner = models.CharField(
        choices=WinnerStatus.choices, max_length=6, blank=True)
    userOnePoints = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, default=0)
    userTwoPoints = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, default=0)
    startAt = models.DateTimeField(auto_now=True)
    finishAt = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        choices=GameStatus.choices, max_length=10, default=GameStatus.IN_PROCESS)
    moves = models.JSONField(default=dict, blank=True)


class Move(models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='game')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    checkerId = models.PositiveSmallIntegerField()
    newPositions = models.JSONField(default=list, blank=True)
    isKing = models.BooleanField(default=False)
    isLastMove = models.BooleanField(default=True)
    isWhite = models.BooleanField(default=True)
    isDead = models.BooleanField(default=False)
