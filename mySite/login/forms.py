from django.forms import ModelForm
from login.models import registerModel
from django import forms

class registerForm(ModelForm):
    class Meta:
        model = registerModel
        fields = ["email", "username", "password", "repeatpassword"]
        
    