from pydantic import BaseModel, field_validator, Field
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

class Point(BaseModel):
  
  latitude: float = Field(
        ..., description='Latitude of the location', example=45.754114
    )
  longitude: float = Field(
        ..., description='Longitude of the location',example=4.860374
    )
  
  @classmethod
  def get_coordinates(cls,address: str):
    """
    Geocodes an address using Nominatim.

    Args:
      address: The address string to geocode.

    Returns:
      A tuple containing latitude and longitude, or None if geocoding fails.
    """
    geolocator = Nominatim(user_agent="my_geocoder")
    try:
      location = geolocator.geocode(address)
      if location:
        return cls(latitude = location.latitude, longitude = location.longitude)
      else:
        return None
    except Exception as e:
      print(f"Geocoding error: {e}")
      return None