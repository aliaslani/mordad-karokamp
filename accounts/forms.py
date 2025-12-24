from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

# class RegisterForm(forms.ModelForm):
#     p1 = forms.CharField(
#         max_length=30,
#         widget=forms.PasswordInput(attrs={"class": "form-control"}),
#         label="گذرواژه",
#     )
#     p2 = forms.CharField(
#         max_length=30,
#         widget=forms.PasswordInput(attrs={"class": "form-control"}),
#         label="تکرار گذرواژه ",
#     )


#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "email",
#         ]

#     def clean(self):
#         data = super().clean()
#         p1 = data.get("p1")
#         p2 = data.get("p2")
#         if p1 and p2 and p1 != p2:
#             raise ValidationError("گذرواژه با تکرار آن مطابقت ندارد")

#         validate_password(p1)
#         return data

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data.get("p1"))
#         user.save()
#         return user


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=40,
        label="نام کاربری",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}), label="گذرواژه"
    )
