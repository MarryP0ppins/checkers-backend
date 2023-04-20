# Generated by Django 4.1.3 on 2023-04-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_move_is_king'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(
                choices=[
                    ('CREATED',
                     'Создана'),
                    ('IN_PROCESS',
                     'В процессе'),
                    ('FINISHED',
                     'Закончена')],
                max_length=10),
        ),
        migrations.AlterField(
            model_name='move',
            name='checker_id',
            field=models.PositiveSmallIntegerField(),
        ),
    ]