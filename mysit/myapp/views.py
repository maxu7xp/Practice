from django.http import HttpResponse
from myapp.forms import ContactForm
from django.shortcuts import render

def contact(request):
    form = ContactForm
    return render(request, 'form.html', {'form': form})
