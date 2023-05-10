from django.db import models


class DocumentFileModel(models.Model):
    class Meta:
        app_label = "categories"
        verbose_name = "File"
        verbose_name_plural = "Files"

    name = models.CharField(
        max_length=256,
        verbose_name="Nombre",
        help_text="Nombre del documento/archivo"
    )
    file = models.FileField(
        upload_to='data/categories/documents/',
        verbose_name="Archivo"
    )

    def __str__(self):
        return self.name
