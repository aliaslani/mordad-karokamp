from django.db import models


class CityChoices(models.TextChoices):
    TEHRAN = ("tehran", "تهران")
    ISFAHAN = ("isfahan", "اصهان")


class ShowToChoices(models.TextChoices):
    NOBODY = ("nobody", "هیچکس")
    CLOSEFRIENDS = ("closefriends", "دوستان صمیمی")
    ALL = ("all", "همه")


class GenderChoices(models.TextChoices):
    MALE = ("male", "مرد")
    FEMALE = ("female", "زن")


class CategoryChoices(models.TextChoices):
    SOCIAL = ("social", "اجتماعی")
    SPORT = ("sport", "ورزشی")


class User(models.Model):
    username = models.CharField(max_length=32, unique=True, verbose_name="نام کاربری")
    password = models.CharField(max_length=20)
    birthdate = models.DateField(null=True)
    bio = models.TextField(null=True)
    city = models.CharField(
        max_length=20, choices=CityChoices.choices, default=CityChoices.ISFAHAN
    )
    email = models.EmailField("ایمیل")
    close_friend = models.ManyToManyField(to="self", null=True, blank=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"


admin_user = User.objects.filter(username="admin").first()


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=False)
    show_to = models.CharField(
        max_length=20, choices=ShowToChoices.choices, default=ShowToChoices.NOBODY
    )
    is_deleted = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CategoryChoices)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست"
