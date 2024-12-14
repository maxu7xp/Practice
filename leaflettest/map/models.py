from django.db import models

class MapLocationMarkers(models.Model):
    IsHuis = models.FloatField()
    IsKantoor = models.FloatField()
    IsRave = models.FloatField()
    MarkerLatitude = models.FloatField()
    MarkerLongtitude = models.FloatField()
