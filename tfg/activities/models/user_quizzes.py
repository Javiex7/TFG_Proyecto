from django.db import models
from django.contrib.auth.models import User

from .quizzes import QuizModel


class UserQuizModel(models.Model):
    class Meta:
        app_label = "activities"
        verbose_name = "User quiz"
        verbose_name_plural = "User quizzes"

    quiz = models.ForeignKey(
        QuizModel,
        related_name='user_quizzes',
        on_delete=models.CASCADE,
        verbose_name="Quiz"
    )

    user = models.ForeignKey(
        User,
        related_name='user_quizzes',
        on_delete=models.CASCADE,
        verbose_name="Usuario"
    )

    tries = models.IntegerField(
        verbose_name="Intentos sobre el quiz actual",
        default=0
    )

    correct_answers = models.IntegerField(
        verbose_name="Respuestas/puntos consegidos con este quiz",
        default=0
    )

    best_time = models.DurationField(
        verbose_name="Mejor tiempo",
        help_text="Mejor tiempo conseguido por el usuario en este quiz",
        null=True,
        blank=True
    )
