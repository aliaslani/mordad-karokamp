from datetime import datetime
from xml.dom import ValidationErr
from django import forms
from core.models import CityChoices, CategoryChoices
from core.models import User, Post


# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=4,
#         required=True,
#         label="عنوان",
#         validators=[
#             validators.MinLengthValidator(
#                 3, "این فیلد نمی تواند کمتر از ۳ کاراکتر باشد"
#             )
#         ],
#     )
#     content = forms.CharField(max_length=255)
#     username = forms.CharField(max_length=50)
#     user = forms.ModelChoiceField(queryset=User.objects.all())
#     visible = forms.BooleanField()
#     category = forms.ChoiceField(choices=CategoryChoices.choices)

#     def clean_content(self):
#         d = self.cleaned_data.get("content")
#         absurd_words = ["hello", "hi", "bye"]
#         for word in absurd_words:
#             if word in d:
#                 raise forms.ValidationError("این حرفها زشت است نزن")
#         return d

#     def clean_title(self):
#         title = self.cleaned_data.get("title")
#         if len(title) == 0:
#             raise forms.ValidationError("این فیلد نمی تواند خالی باشد")
#         return title


class PostForm(forms.ModelForm):
    tag = forms.CharField(
        max_length=40, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}),
        label="تست عنوان",
        help_text="اینجا باید عنوان پست را بنویسی",
    )
    # category = forms.ChoiceField(
    #     widget=forms.RadioSelect(attrs={"class": "form-radio"}),
    #     initial=CategoryChoices.SOCIAL,
    #     choices=CategoryChoices.choices,
    # )

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "user",
            "visible",
            "image",
            "show_to",
            "category",
            "tag",
        ]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-radio"}),
        }
        error_messages = {
            "title": {
                "required": "این فیلد اجباری است",
                "max-length": "این فیلد نمی تواند بیشتر از ۳۰ کاراکتر باشد",
            }
        }

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 3:
            raise forms.ValidationError(
                "این فیلد نمی تواند کمتر از ۳ کاراکتر داشته باشد"
            )
        return content

    def clean(self):
        data = super().clean()
        title = data.get("title")
        content = data.get("content")
        if title not in content:
            raise forms.ValidationError("حتما باید عنوان در محتوا هم باشد")
        return data


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=30, label="نام کاربری")
    password = forms.CharField(
        max_length=40,
        label="گذرواژه",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "گذرواژه"},
        ),
    )
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    bio = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    city = forms.ChoiceField(choices=CityChoices.choices, initial=CityChoices.ISFAHAN)
    email = forms.EmailField()
    close_friend = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check"}),
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


class EditPostForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=CategoryChoices.choices,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-control", "disabled": "on"}),
    )

    class Meta:
        model = Post
        fields = ["content", "show_to", "visible", "image", "category", "user"]
