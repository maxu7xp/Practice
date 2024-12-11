from django.db import models

class MapLocationMarkers(models.Model):
    IsHuis = models.FloatField()
    isKantoor = models.FloatField()
    IsRave = models.FloatField()
    MarkerLatitude = models.FloatField()
    MarkerLongtitude = models.FloatField()
