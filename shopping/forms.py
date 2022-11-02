from django.forms import ModelForm
from shopping.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']