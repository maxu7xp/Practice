from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, authenticate
from .forms import loginForm

def succes(request):
    return render(request, "authTemplates/success.html")

def mylogin(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect('success')
            
            else:
                raise Http404

    else:
        form = loginForm()
    
    return render(request, "authTemplates/login.html", {"form": form})