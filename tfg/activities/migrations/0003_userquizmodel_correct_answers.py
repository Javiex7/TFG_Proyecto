# Generated by Django 4.1.4 on 2023-05-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0002_alter_questionmodel_correct_option"),
    ]

    operations = [
        migrations.AddField(
            model_name="userquizmodel",
            name="correct_answers",
            field=models.IntegerField(
                default=0, verbose_name="Respuestas/puntos consegidos con este quiz"
            ),
        ),
    ]
