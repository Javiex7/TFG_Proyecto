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
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Quiz"
    )

    user = models.ForeignKey(
        User,
        related_name='user_quizzes',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Usuario"
    )
