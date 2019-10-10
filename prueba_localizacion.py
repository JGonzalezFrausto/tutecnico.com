from geopy.geocoders import Nominatim #geolocalizador 

geolocalizador = Nominatim()
ubicacion = geolocalizador.reverse("21.1526503,-101.6777939")
print(ubicacion.address)


from 