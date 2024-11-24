from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authenticate/register_user.html')
    else:
        return render(request, 'authenticate/login.html', {})
    

def register_user(request):
    return render(request,'authenticate/register_user.html', {})
    