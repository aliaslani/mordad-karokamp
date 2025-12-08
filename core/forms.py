from datetime import timedelta, datetime
from tkinter import Widget
from django import forms
from core.models import CategoryChoices, CityChoices
from django.core import validators
from core.models import User, Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=4,
        required=True,
        label="عنوان",
        validators=[
            validators.MinLengthValidator(
                3, "این فیلد نمی تواند کمتر از ۳ کاراکتر باشد"
            )
        ],
    )
    content = forms.CharField(max_length=255)
    username = forms.CharField(max_length=50)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    visible = forms.BooleanField()
    category = forms.ChoiceField(choices=CategoryChoices.choices)

    def clean_content(self):
        d = self.cleaned_data.get("content")
        absurd_words = ["hello", "hi", "bye"]
        for word in absurd_words:
            if word in d:
                raise forms.ValidationError("این حرفها زشت است نزن")
        return d

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) == 0:
            raise forms.ValidationError("این فیلد نمی تواند خالی باشد")
        return title


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=30, label="نام کاربری")
    password = forms.CharField(
        max_length=40,
        label="گذرواژه",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "گذرواژه"},
        ),
    )
    birthdate = forms.DateField()
    bio = forms.Textarea()
    city = forms.ChoiceField(choices=CityChoices.choices, initial=CityChoices.ISFAHAN)
    email = forms.EmailField()
    close_friend = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-checkbox"}),
    )

    def clean_birthdate(self):
        bd = self.cleaned_data.get("birthdate")
        if (datetime.now().date() - bd).days < 18 * 365:
            # if bd > (datetime.now().date() - timedelta(years=18)):
            raise forms.ValidationError("کاربر بچه سال قبول نمی کنیم")

        return bd

    def clean(self):
        data = super().clean()
        username = data.get("username")
        password = data.get("password")
        if username in password:
            raise forms.ValidationError("نام کاربری نمی تواند بخشی از گذرواژه باشد")
        return data
