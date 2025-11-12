from pyexpat import model
from turtle import mode
from django.db import models


class CityChoices(models.TextChoices):
    TEHRAN = ("tehran", "تهران")
    ISFAHAN = ("isfahan", "اصهان")


class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=20)
    birthdate = models.DateField(null=True)
    bio = models.TextField(null=True)
    city = models.CharField(
        max_length=20, choices=CityChoices.choices, default=CityChoices.ISFAHAN
    )
