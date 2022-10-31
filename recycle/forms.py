from django import forms
from recycle.models import RecycleHistory

dropoff_choices = [
    ('AEON Serpong', 'AEON Serpong'),
    ('Botani Square', 'Botani Square'),
    ('Kota Kasablanka', 'Kota Kasablanka'),
    ('Margocity Depok', 'Margocity Depok'),
    ('Paris Van Java', 'Paris Van Java'),
    ('Plaza Indonesia', 'Plaza Indonesia'),
    ('Senayan City', 'Senayan City'),
    ('Summarecon Bekasi', 'Summarecon Bekasi')
]

class DropOffForm(forms.ModelForm):
    class Meta:
        model = RecycleHistory
        fields = ('name', 'weight', 'location', 'description') 
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Enter the plastic weight'}),
            'location': forms.RadioSelect(choices=dropoff_choices),
            'description': forms.Textarea(attrs={'placeholder': 'Tell us your experience with PlasTIX'})
        }
    
class PickUpForm(forms.ModelForm):
    class Meta:
        model = RecycleHistory
        fields = ('name', 'weight', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Enter the plastic weight'}),
            'description': forms.Textarea(attrs={'placeholder': 'Tell us your experience with PlasTIX'})
        }
    
    region = forms.CharField(label="Region", 
                            widget=forms.TextInput(attrs={'placeholder': 'Jawa Barat'}))
    city = forms.CharField(label="City", 
                            widget=forms.TextInput(attrs={'placeholder': 'Bogor'}))
    subdistrict = forms.CharField(label="Subdistrict", 
                                widget=forms.TextInput(attrs={'placeholder': 'Cileungsi'}))
    zip_code = forms.IntegerField(label="ZIP Code", 
                                widget=forms.NumberInput(attrs={'placeholder': '12345'}))
    address_detail = forms.CharField(label="Details",
                                    widget=forms.TextInput(attrs={'placeholder': 'Street Name, Building Number'}))
   