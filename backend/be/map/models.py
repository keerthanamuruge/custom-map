from django.db import models


class MapLocationManager():
    def create_place_name(self, place_name):
        map = self.model(
            place_name = place_name
        )
        map.save()
        return map
    def create_loc(self, id, latitude, longitude,):
        map = MapLocation.objects.get(id = id)
        map.latitude = latitude
        map.longitude = longitude
        map.save()
        return map


class MapLocation(models.Model):
    id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=100, null=True)
    longitude = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.id