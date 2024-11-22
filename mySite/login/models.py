from django.db import models

class loginModel(models.Model):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    
    
