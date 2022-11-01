from news.models import NewsData
from django.forms import ModelForm
class FormTask(ModelForm):
    class Meta:
        model = NewsData
        fields = ('user', 'date', 'title', 'description')
        exclude = ['user', 'date']