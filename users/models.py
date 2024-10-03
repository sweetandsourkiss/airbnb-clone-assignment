from hashlib import blake2b
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
    )
    avatar = models.ImageField(
        blank=True,
    )
    name = models.CharField(
        max_length=150,
        default="",
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name}"
