from geopy.geocoders import Nominatim

def get_coordinates(lieu):
    geolocator = Nominatim(user_agent="weather-simulator-app")
    location = geolocator.geocode(lieu)
    if location is None:
        raise ValueError(f"Lieu introuvable : {lieu}")
    return location.latitude, location.longitude
