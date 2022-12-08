from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Título",
        help_text="Título de la categoría"
    )
    content = models.TextField(
        max_length=32768,
        verbose_name="Contenido teórico",
        help_text="Contenido teórico básico",
        null=True,
        blank=True
    )
    active = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"#{self.id} - {self.title}"
