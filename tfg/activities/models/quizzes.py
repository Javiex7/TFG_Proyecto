from django.db import models

from categories.models import CategoryModel
from .questions import QuestionModel


class QuizModel(models.Model):
    class Meta:
        app_label = "activities"
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    name = models.CharField(
        max_length=256,
        verbose_name="Nombre",
        help_text="Nombre del quiz"
    )
    description = models.CharField(
        max_length=256,
        verbose_name="Descripción",
        help_text="Pequeña descripción del quiz",
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        CategoryModel,
        related_name='quizzes',
        on_delete=models.SET_NULL,
        verbose_name="Categoría",
        help_text="Categoría del quiz",
        null=True,
        blank=True
    )
    max_tries = models.PositiveIntegerField(
        verbose_name="Intentos",
        help_text="Número máximo de intentos para realizar el cuestionario",
        default=3
    )
    code = models.CharField(
        max_length=256,
        verbose_name="Código",
        help_text="Código para identificar rápidamente preguntas/quiz",
        null=True,
        blank=True
    )
    questions = models.ManyToManyField(
        QuestionModel,
        related_name="quizzes"
    )
    active = models.BooleanField(
        verbose_name="Activo",
        default=True,
    )

    def __str__(self):
        if (self.code):
            return '%s - %s' % (self.code, self.name)
        return self.name
