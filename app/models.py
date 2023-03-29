from django.db import models
from authentication.models import User


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    rating = models.PositiveSmallIntegerField(default=0)


class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    username_1 = models.CharField(db_index=True, max_length=16)
    username_2 = models.CharField(db_index=True, max_length=16)
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(null=True)
    moves = models.JSONField(default=dict)
