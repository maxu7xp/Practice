from django.shortcuts import render
from django.http import HttpResponse, Http404
from login.forms import registerForm

def view(request, ):
    
    return HttpResponse()

def register(request):
        if request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                form.save()
                
                
                
        return render(request, "register.html", {"form": registerForm()})