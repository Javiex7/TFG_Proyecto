from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    points = models.IntegerField(
        verbose_name="Puntos actuales",
        default=0
    )

    obtained_points = models.IntegerField(
        verbose_name="Puntos obtenidos",
        default=0
    )

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not Profile:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
