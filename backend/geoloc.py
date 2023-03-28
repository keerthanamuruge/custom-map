from geopy.geocoders import ArcGIS
import folium
nom=ArcGIS()
location = nom.geocode("Tamil Nadu, India")
map=folium.Map(location=[location.latitude, location.longitude],zoom_start=50)
map.save("map.html")