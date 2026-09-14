from dataclasses import dataclass
from datetime import datetime

@dataclass
class Satellite:
    sat_id: int
    norad_id: int
    name: str
    latitude: float
    longitude: float
    altitude_in_km: float
    timeline: datetime
    velocity: float
    visibility: str
    location: str