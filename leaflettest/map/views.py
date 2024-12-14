from django.shortcuts import render
from .forms import TypeOfLocation
from map.models import MapLocationMarkers

def myMap(request):
    if request.method == "POST":
        form = TypeOfLocation(request.POST)
        if form.is_valid():
            MapFilterFormAnswer = form.cleaned_data["dropDownLocationButton"]
            print(MapFilterFormAnswer)
            if MapFilterFormAnswer == "huis":
                
                ## here we retrieve the right items for the db.  by checking if isHuis is set to 1
                MarkersToPlace = MapLocationMarkers.objects.exclude(IsHuis = 0)
                MarkerLocations = list(MarkersToPlace.values("MarkerLatitude", "MarkerLongtitude"))
                
                return render(request, "map.html", {"form": form, "MarkersLocation": MarkerLocations},)
        
    form = TypeOfLocation
    return render(request, "map.html", {"form": form})