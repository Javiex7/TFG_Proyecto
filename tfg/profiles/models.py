from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from categories.models.point_packs import PointPackModel


class Profile(models.Model):
    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    group = models.CharField(
        max_length=256,
        verbose_name="Grupo",
        null=True,
        blank=True
    )

    points = models.IntegerField(
        verbose_name="Puntos actuales",
        default=0
    )

    obtained_points = models.IntegerField(
        verbose_name="Puntos obtenidos",
        default=0
    )

    purchased_packs = models.ManyToManyField(
        PointPackModel,
        related_name="profiles",
        help_text="Paquetes de muestras/imágenes obtenidos por el usuario",
        blank=True
    )

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # instace = user
    # Check if there's already a related profile Profile(user=instance)
    if not Profile.objects.filter(user=instance):
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
