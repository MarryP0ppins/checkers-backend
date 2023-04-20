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
        CREATED = 'CREATED', _('Создана')
        IN_PROCESS = 'IN_PROCESS', _('В процессе')
        FINISHED = 'FINISHED', _('Закончена')

    id = models.BigAutoField(primary_key=True)
    user_1 = models.ForeignKey(
        User, on_delete=models.SET(get_unknown_user), related_name='user_1')
    user_2 = models.ForeignKey(
        User, on_delete=models.SET(get_unknown_user), related_name='user_2')
    user_1_turn = models.BooleanField(default=True)
    start_at = models.DateTimeField(null=True, blank=True)
    finish_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        choices=GameStatus.choices, max_length=10, default=GameStatus.CREATED)
    moves = models.JSONField(default=dict, null=True, blank=True)


class Move(models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='game')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    checker_id = models.PositiveSmallIntegerField()
    new_positions = models.JSONField(default=list, null=True, blank=True)
    is_king = models.BooleanField(default=False)
    is_last_move = models.BooleanField(default=True)
    is_white = models.BooleanField(default=True)
