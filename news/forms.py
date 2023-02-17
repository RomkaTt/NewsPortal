from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError("Новость не должно быть идентично названию новости.")
        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Новость не должно быть идентично названию новости."
            )
        return cleaned_data
