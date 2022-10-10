from django import forms
from .models import *


class AddPostForm(forms.Form):
    slug = forms.SlugField(max_length=255, label='URL')
    title = forms.CharField(max_length=255, label='Заголовок')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Контент')
    is_publisher = forms.BooleanField(label='Публикация', required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категория', empty_label='Категория не выбрана')