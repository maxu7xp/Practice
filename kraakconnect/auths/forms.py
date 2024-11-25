from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label="your name", max_length="15")
    password = forms.CharField(widget=forms.PasswordInput)