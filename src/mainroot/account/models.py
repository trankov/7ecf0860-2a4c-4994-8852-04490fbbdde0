from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Inherits from generic Django Auth class to add nessessary fields
    """

    class Meta(AbstractUser.Meta):
        # Comes from original Django Auth declaration
        swappable = "AUTH_USER_MODEL"

    patronymic = models.CharField(
        verbose_name="Отчество",
        max_length=64,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=64,
        null=True,
        blank=True,
    )
