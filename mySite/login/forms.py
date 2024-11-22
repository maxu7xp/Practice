from django.forms import ModelForm
from login.models import loginModel

class loginForm(ModelForm):
    class Meta:
        model = loginModel
        fields = ["email", "username", "password"]