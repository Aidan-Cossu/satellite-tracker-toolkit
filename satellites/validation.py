from datetime import datetime
from database.database import get_satellites as get_database_satellites
from dataclasses import dataclass

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

def validate_satellites():
    rows = get_database_satellites()

    for row in rows:
        sat_id, norad_id, name, latitude, longitude, altitude_in_km, timeline, velocity, visibility, location = row

        if sat_id is None or not isinstance(sat_id, int):
            raise ValueError("Every satellite must have a unique satellite id, and must be an integer")

        if norad_id is None or not isinstance(norad_id, int):
            raise ValueError("Every satellite must have a unique NORAD id, and it must be an integer")

        if name is None or not isinstance(name, str):
            raise ValueError("Every satellite must have a name")

        if latitude is None or not isinstance(latitude, (int, float)):
            raise ValueError("Every satellite must have a latitude")

        if longitude is None or not isinstance(longitude, (int, float)):
            raise ValueError("Every satellite must have a longitude")

        if altitude_in_km is None or not isinstance(altitude_in_km, (int, float)):
            raise ValueError("Every satellite must have a altitude_in_km")

        if timeline is None or not isinstance(timeline, str):
            raise ValueError("Every satellite must have a timeline")

        if velocity is None or not isinstance(velocity, (int, float)):
            raise ValueError("Every satellite must have a velocity")

        if visibility is None or not isinstance(visibility, str) or visibility not in ("daylight", "eclipsed"):
            raise ValueError("Every satellite must have a visibility")

        if location is None or not isinstance(location, str):
            raise ValueError("Every satellite must have a location")

        if not -90 <= latitude <= 90:
            raise ValueError("Every satellite must be between -90 and 90 degrees")

        if not -180 <= longitude <= 180:
            raise ValueError("Every satellite must be between -180 and 180 degrees")

        if altitude_in_km < 0:
            raise ValueError("Altitude cannot be negative")

    return rows

def create_satellites():
    rows = validate_satellites()

    satellites = []

    for row in rows:
        (
            sat_id,
            norad_id,
            name,
            latitude,
            longitude,
            altitude_in_km,
            timeline,
            velocity,
            visibility,
            location
        ) = row

        satellite = Satellite(
            sat_id,
            norad_id,
            name,
            latitude,
            longitude,
            altitude_in_km,
            timeline,
            velocity,
            visibility,
            location
        )

        satellites.append(satellite)

    return satellites

def clean_satellites():
    satellites = create_satellites()

    for satellite in satellites:
        satellite.name = satellite.name.strip()
        satellite.latitude = round(satellite.latitude, 3)
        satellite.longitude = round(satellite.longitude, 3)
        satellite.altitude_in_km = round(satellite.altitude_in_km, 3)
        satellite.velocity = round(satellite.velocity, 3)
        satellite.visibility = satellite.visibility.lower()
        satellite.timeline = datetime.fromisoformat(satellite.timeline.split("[")[0])

    return satellites
