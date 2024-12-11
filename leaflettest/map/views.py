from django.shortcuts import render
from .forms import TypeOfLocation

def myMap(request):
    form = TypeOfLocation
    return render(request, "map.html", {"form": form})