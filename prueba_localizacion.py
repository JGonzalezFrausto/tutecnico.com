from geopy.geocoders import Nominatim #geolocalizador 
from geopy import distance


jardines_del_moral = ("21.1466363,-101.6924656")
haciendas_del_rosario = ("21.1536054,-101.6529349")
obregon = ("21.1322351,-101.6916145")
san_jeronimo = ("21.1262232,-101.6733762")
andrade = ("21.1146037,-101.6770974")

print (distance.distance ( haciendas_del_rosario , jardines_del_moral ).km)
print (distance.distance(obregon,san_jeronimo).m)
