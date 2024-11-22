from django.shortcuts import render
from django.http import HttpResponse
from login.forms import loginForm

def view(request, ):
    
    return HttpResponse()

def login(request):
    return render(request, "login.html", {"form": loginForm})