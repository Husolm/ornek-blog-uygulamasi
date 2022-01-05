from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import Article
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','article_images']
