from django.db import models


class CustomImageModel(models.Model):
    class Meta:
        app_label = "categories"
        verbose_name = "Pack image"
        verbose_name_plural = "Pack images"

    name = models.CharField(
        max_length=256,
        verbose_name="Nombre",
        default="P_IMG"
    )
    code = models.CharField(
        max_length=256,
        verbose_name="Código",
        help_text="Código para identificar rápidamente paquetes/imágenes",
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='data/categories/pack_images/',
        verbose_name="Imagen",
    )

    def __str__(self):
        if (self.code):
            return '%s - %s' % (self.code, self.name)
        return self.name


class PointPackModel(models.Model):
    class Meta:
        app_label = "categories"
        verbose_name = "Point Pack"
        verbose_name_plural = "Point packs"

    name = models.CharField(
        max_length=256,
        verbose_name="Nombre",
        help_text="Nombre del paquete de muestras"
    )
    code = models.CharField(
        max_length=256,
        verbose_name="Código",
        help_text="Código para identificar rápidamente paquetes/imágenes",
        null=True,
        blank=True
    )
    price = models.IntegerField(
        verbose_name="Precio",
        help_text="Precio del paquete (en puntos)",
        default=5
    )
    images = models.ManyToManyField(
        CustomImageModel,
        verbose_name="Muestras",
        related_name="pointpacks",
        blank=True,
        help_text="Muestras/Imágenes disponibles dentro del pack"
    )
    active = models.BooleanField(
        verbose_name="Activo",
        default=True,
    )

    def __str__(self):
        if (self.code):
            return self.code
        return self.name
