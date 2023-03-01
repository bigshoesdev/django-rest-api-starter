from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    info = models.TextField(
        default="",
        blank=True,
    )
