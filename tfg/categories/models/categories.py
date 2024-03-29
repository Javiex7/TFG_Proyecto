from django.db import models

from categories.models.documents_files import DocumentFileModel
from categories.models.point_packs import PointPackModel


class CategoryModel(models.Model):
    class Meta:
        app_label = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    title = models.CharField(
        max_length=256,
        verbose_name="Título",
        help_text="Título de la categoría"
    )
    short_description = models.CharField(
        max_length=1024,
        verbose_name="Descripción corta",
        help_text="Pequeña descripción de la categoría"
    )
    content = models.TextField(
        max_length=32768,
        verbose_name="Contenido teórico",
        help_text="Contenido 'teórico' incluido en la página de la categoría",
        null=True,
        blank=True
    )
    files = models.ManyToManyField(
        DocumentFileModel,
        related_name="categories_file",
        help_text="Archivos adicionales asignados a esta categoría",
        blank=True
    )
    packs = models.ManyToManyField(
        PointPackModel,
        related_name="categories_pack",
        help_text="Paquetes de muestras/imágenes asociados a esta categoría",
        blank=True
    )
    image = models.ImageField(
        upload_to='data/categories/display_images/',
        verbose_name="Imagen",
        null=True,
        blank=True
    )
    order = models.PositiveIntegerField(
        verbose_name="Orden",
        default=0,
    )
    active = models.BooleanField(
        verbose_name="Activa",
        default=True,
    )
    generic = models.BooleanField(
        verbose_name="General",
        help_text="Indica si se utilizará para para quizzes/elementos sin categoría específica",
        default=False,
    )

    def __str__(self):
        return self.title
