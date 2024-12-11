from django.shortcuts import render
from .forms import TypeOfLocation
from map.models import MapLocationMarkers

def myMap(request):
    form = TypeOfLocation
    MarkersToPlace = list(MapLocationMarkers.objects.values("MarkerLatitude", "MarkerLongtitude"))
    return render(request, "map.html", {"form": form})