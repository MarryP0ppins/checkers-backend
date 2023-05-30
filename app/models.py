from django.db import models
from authentication.models import User
from django.utils.translation import gettext_lazy as _


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
    user_1 = models.ForeignKey(
        User, on_delete=models.SET(get_unknown_user), related_name='user_1')
    user_2 = models.ForeignKey(
        User, on_delete=models.SET(get_unknown_user), related_name='user_2')
    user_1_turn = models.BooleanField(default=True)
    winner = models.CharField(
        choices=WinnerStatus.choices, max_length=6, blank=True)
    user_1_points = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True)
    user_2_points = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True)
    start_at = models.DateTimeField(auto_now=True)
    finish_at = models.DateTimeField(blank=True)
    status = models.CharField(
        choices=GameStatus.choices, max_length=10, default=GameStatus.IN_PROCESS)
    moves = models.JSONField(default=dict, blank=True)


class Move(models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='game')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    checker_id = models.PositiveSmallIntegerField()
    new_positions = models.JSONField(default=list, blank=True)
    is_king = models.BooleanField(default=False)
    is_last_move = models.BooleanField(default=True)
    is_white = models.BooleanField(default=True)
    is_dead = models.BooleanField(default=False)
