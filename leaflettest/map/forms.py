from django import forms

LocationSelection = [
    ('IsHuis', 'Huis'),
    ('kantoor', 'Kantoor'),
    ('rave', 'Rave'),
    ]
    
class TypeOfLocation(forms.Form):
    
    dropDownLocationButton = forms.ChoiceField(choices=LocationSelection)
    

        