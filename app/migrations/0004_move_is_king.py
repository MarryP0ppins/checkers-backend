# Generated by Django 4.1.3 on 2023-04-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_game_finish_at_alter_game_moves_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='is_king',
            field=models.BooleanField(default=False),
        ),
    ]