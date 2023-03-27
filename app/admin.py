from django.contrib import admin
from .models import *


@admin.register(Profile)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'games', 'wins', 'rating')
