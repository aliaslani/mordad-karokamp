from django.db import models
from datetime import datetime
from accounts.models import User


class ShowToChoices(models.TextChoices):
    NOBODY = ("nobody", "هیچکس")
    CLOSEFRIENDS = ("closefriends", "دوستان صمیمی")
    ALL = ("all", "همه")


class CategoryChoices(models.TextChoices):
    SOCIAL = ("social", "اجتماعی")
    SPORT = ("sport", "ورزشی")


# class Profile(models.Model):
#     user = models.OneToOneField(
#         to=User, on_delete=models.CASCADE, verbose_name="کاربر", related_name="profile"
#     )
#     birthdate = models.DateField(null=True)
#     bio = models.TextField(null=True)
#     city = models.CharField(
#         max_length=20, choices=CityChoices.choices, default=CityChoices.ISFAHAN
#     )
#     close_friend = models.ManyToManyField(to="self", null=True, blank=True)
#     gender = models.CharField(max_length=10, choices=GenderChoices)
#     profile_picture = models.ImageField(
#         upload_to="profile_pictures", default="profile_pictures/avatar.jpg"
#     )

#     def __str__(self):
#         return f"{self.username}"

#     class Meta:
#         verbose_name = "کاربر"
#         verbose_name_plural = "کاربر"


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    content = models.TextField()
    user = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=False)
    show_to = models.CharField(
        max_length=20, choices=ShowToChoices.choices, default=ShowToChoices.NOBODY
    )
    is_deleted = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CategoryChoices)
    image = models.ImageField(
        upload_to=f"post_pictures/{datetime.now().strftime('%Y%m%d')}",
        null=True,
        blank=True,
    )

    def has_image(self):
        if self.image and self.image.url:
            return True
        return False

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست"


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="کاربر", related_name="likes"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="پست")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک"

    def __str__(self):
        return f"{self.post}-{self.user}"
