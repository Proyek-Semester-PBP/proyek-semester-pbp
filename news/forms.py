from django import forms
from news.models import NewsData
from django.forms import ModelForm
class FormPage(ModelForm):
    class Meta:
        model = NewsData
        fields = ('title', 'date')