from pydantic import BaseModel, field_validator, Field
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from pathlib import Path
import yaml

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
    # Load user agent from config.yaml if available
    user_agent = "my_geocoder"
    try:
      here = Path(__file__).resolve()
      for p in [here.parent, here.parent.parent, here.parent.parent.parent]:
        cfg_file = p / "config.yaml"
        if cfg_file.exists():
          with cfg_file.open("r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
          user_agent = ((cfg.get("geocoding") or {}).get("nominatim_user_agent")) or user_agent
          break
    except Exception:
      pass

    geolocator = Nominatim(user_agent=user_agent)
    try:
      location = geolocator.geocode(address)
      if location:
        return cls(latitude = location.latitude, longitude = location.longitude)
      else:
        return None
    except Exception as e:
      print(f"Geocoding error: {e}")
      return None