from django.db import models

from categories.models import CategoryModel


class ActivityModel(models.Model):
    class ActivityTypes(models.IntegerChoices):
        THEORY = 1, 'Theory'
        QUIZ = 2, 'Quiz'

    title = models.CharField(
        max_length=256,
        verbose_name="Título",
        help_text="Título de la actividad"
    )
    type = models.PositiveSmallIntegerField(
        choices=ActivityTypes.choices,
        default=ActivityTypes.THEORY,
        verbose_name="Tipo",
        help_text="Tipo de actividad"
    )
    category = models.ForeignKey(
        CategoryModel,
        related_name='actividades',
        on_delete=models.SET_NULL,
        verbose_name="Categoría",
        help_text="Categoría de la actividad",
        null=True,
        blank=True
    )
    active = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"#{self.id} - {self.title}"
