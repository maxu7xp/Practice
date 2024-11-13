from django.http import HttpResponse
from myapp.forms import ContactForm, SnippetForm
from django.shortcuts import render

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        print(form.is_valid())
        
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            print(name, email)
            
    
    form = ContactForm()
    return render(request, 'form.html', {'form': form})



def snippet_detail(request):
    
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        
        if form.is_valid():
            print("VALID")
            form.save()
            
    
    form = SnippetForm()
    return render(request, 'form.html', {'form': form})
    