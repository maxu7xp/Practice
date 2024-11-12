from django import forms
from .models import Snippet

class ContactForm(forms.Form):
    name = forms.CharField() 
    email = forms.EmailField(label="E-Mail")
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other'),('me', 'Me')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
    
class snippetForm(forms.ModelForm):
    class meta:
        model = Snippet
        fields = ('name', 'body')