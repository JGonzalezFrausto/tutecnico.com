from geopy.geocoders import Nominatim #geolocalizador para obtener direcciones y latitud,longitud
from geopy import distance

geolocalizador = Nominatim() #dejar lista de argumentos vacia
localizacion = geolocalizador.reverse ("21.1466363,-101.6924656")# con reverse se obtene la dirección apartir de coordenadas 
colonia = geolocalizador.geocode ("Haciendas del Rosario") #obtiene coordenadas
print (localizacion.address)
print (( colonia.latitude, colonia.longitude))

jardines_del_moral = ("21.1466363,-101.6924656")
haciendas_del_rosario = ("21.1536054,-101.6529349")
obregon = ("21.1322351,-101.6916145")
san_jeronimo = ("21.1262232,-101.6733762")
andrade = ("21.1146037,-101.6770974")

print (distance.distance ( haciendas_del_rosario , jardines_del_moral ).km)
print (distance.distance ( haciendas_del_rosario , jardines_del_moral ).m)

print (distance.distance ( haciendas_del_rosario , andrade ).m)
