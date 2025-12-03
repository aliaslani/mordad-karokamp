from django import forms
from core.models import CategoryChoices
from django.core import validators


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=4,
        label="عنوان",
        validators=[
            validators.MinLengthValidator(
                3, "این فیلد نمی تواند کمتر از ۳ کاراکتر باشد"
            )
        ],
    )
    content = forms.CharField(max_length=255)
    username = forms.CharField(max_length=50)
    visible = forms.BooleanField()
    category = forms.ChoiceField(choices=CategoryChoices.choices)

    def clean_content(self):
        d = self.cleaned_data.get("content")
        absurd_words = ["hello", "hi", "bye"]
        for word in absurd_words:
            if word in d:
                raise forms.ValidationError("این حرفها زشت است نزن")
        return d
