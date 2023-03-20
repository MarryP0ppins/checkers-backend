from django.db import models

class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    games = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    rating = models.PositiveSmallIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'app_userinfo'