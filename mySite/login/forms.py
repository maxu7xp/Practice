from django.forms import ModelForm
from login.models import loginModel
from django import forms

class loginForm(ModelForm):
    class Meta:
        model = loginModel
        fields = ["email", "username", "password"]
        
    