from rest_framework import serializers

from .models import MapLocation

class MapSerializers(serializers.ModelSerializer):
    class Meta:
        model = MapLocation
        fields = '__all__'