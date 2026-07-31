from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    bio = models.TextField(
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    address = models.CharField(
        max_length=200,
        blank=True,
    )

    def __str__(self):

        return f"{self.user.username}'s Profile"