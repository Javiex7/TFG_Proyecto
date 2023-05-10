# Generated by Django 4.1.4 on 2023-05-10 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoryModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Título de la categoría",
                        max_length=256,
                        verbose_name="Título",
                    ),
                ),
                (
                    "short_description",
                    models.CharField(
                        help_text="Pequeña descripción de la categoría",
                        max_length=1024,
                        verbose_name="Descripción corta",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        help_text="Contenido 'teórico' incluido en la página de la categoría",
                        max_length=32768,
                        null=True,
                        verbose_name="Contenido teórico",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="data/categories/display_images/",
                        verbose_name="Imagen",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Activa")),
                (
                    "generic",
                    models.BooleanField(
                        default=False,
                        help_text="Indica si se utilizará para para quizzes/elementos sin categoría específica",
                        verbose_name="General",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="DocumentFileModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Nombre del documento/archivo",
                        max_length=256,
                        verbose_name="Nombre",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="data/categories/documents/", verbose_name="Archivo"
                    ),
                ),
            ],
            options={
                "verbose_name": "File",
                "verbose_name_plural": "Files",
            },
        ),
    ]
