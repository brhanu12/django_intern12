from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(

        User,

        on_delete=models.CASCADE,

        related_name="profile"

    )

    bio = models.TextField(

        blank=True

    )

    phone = models.CharField(

        max_length=20,

        blank=True

    )

    address = models.CharField(

        max_length=200,

        blank=True

    )

    website = models.URLField(

        blank=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    def __str__(self):

        return self.user.username