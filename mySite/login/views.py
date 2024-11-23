from django.shortcuts import render
from django.http import HttpResponse
from login.forms import registerForm

def view(request, ):
    
    return HttpResponse()

def register(request):
    return render(request, "register.html", {"form": registerForm()})