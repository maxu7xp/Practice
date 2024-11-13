from django import forms
from .models import Snippet

class ContactForm(forms.Form):
    name = forms.CharField() 
    email = forms.EmailField(label="E-Mail")
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other'),('me', 'Me')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
    
class SnippetForm(forms.ModelForm):
    
    #defining it as a Meta class is important because it stands for metadeta and django recognizes this subclass!
    class Meta:
        model = Snippet
        fields = ('name', 'body')