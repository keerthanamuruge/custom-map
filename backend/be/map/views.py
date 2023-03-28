from django.http import HttpResponse, JsonResponse
from geopy.geocoders import ArcGIS
from rest_framework.views import APIView
import folium
from .serializers import MapSerializers
from rest_framework.response import Response
from rest_framework import status

def index(request):
    nom=ArcGIS()
    location = nom.geocode("Tamil Nadu, India")
    map=folium.Map(location=[location.latitude, location.longitude],zoom_start=50)
    map.save("map.html")
    return JsonResponse({"data":map._repr_html_()})


def location(request):
    request.data

class MapLocationView(APIView):
    def post(self, request):
        data=request.data
        serializer = MapSerializers(data=data)
        
        if serializer.is_valid():
            
            location_name = serializer.data['place_name']
            nom=ArcGIS()
            location = nom.geocode(location_name)
            data['latitude'] = location.latitude
            data['longitude'] = location.longitude
            serializer = MapSerializers(data=data)
            serializer.is_valid()
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)