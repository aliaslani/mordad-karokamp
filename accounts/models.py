from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CityChoices(models.TextChoices):
    TEHRAN = ("tehran", "تهران")
    ISFAHAN = ("isfahan", "اصهان")


class GenderChoices(models.TextChoices):
    MALE = ("male", "مرد")
    FEMALE = ("female", "زن")


class User(AbstractUser):
    birthdate = models.DateField(null=True)
    bio = models.TextField(null=True)
    city = models.CharField(
        max_length=20, choices=CityChoices.choices, default=CityChoices.ISFAHAN
    )
    close_friend = models.ManyToManyField(to="self", blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", default="profile_pictures/avatar.jpg"
    )

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"
