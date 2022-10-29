from django import forms

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

class DropOffForm(forms.Form):
    name = forms.CharField(label="Name", 
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    weight = forms.IntegerField(label="Weight",
                                widget=forms.NumberInput(attrs={'placeholder': 'Enter the plastic weight'}))
    location = forms.CharField(label='Location',
                                widget=forms.RadioSelect(choices=dropoff_choices))
    description = forms.CharField(label="Description", required=False,
                                    widget=forms.Textarea(attrs={'placeholder': 'Tell us your experience with PlasTIX'}))

class PickUpForm(forms.Form):
    name = forms.CharField(label="Name", 
                            widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    weight = forms.IntegerField(label="Weight", 
                                widget=forms.NumberInput(attrs={'placeholder': 'Plastic weight in gram'}))
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
    description = forms.CharField(label="Description", required=False,
                                widget=forms.Textarea(attrs={'placeholder': 'Tell us your experience with PlasTIX'}))
