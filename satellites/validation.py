
from datetime import datetime


def validate_satellites(satellites):

    for satellite in satellites:

        if satellite.sat_id is None or not isinstance(satellite.sat_id, int):
            raise ValueError("Every satellite must have a satellite id, and it must be an integer")

        if satellite.norad_id is None or not isinstance(satellite.norad_id, int):
            raise ValueError("Every satellite must have a NORAD id, and it must be an integer")

        if satellite.name is None or not isinstance(satellite.name, str):
            raise ValueError("Every satellite must have a name")

        if satellite.latitude is None or not isinstance(satellite.latitude, (int, float)):
            raise ValueError("Every satellite must have a latitude")

        if satellite.longitude is None or not isinstance(satellite.longitude, (int, float)):
            raise ValueError("Every satellite must have a longitude")

        if satellite.altitude_in_km is None or not isinstance(satellite.altitude_in_km, (int, float)):
            raise ValueError("Every satellite must have an altitude_in_km")

        if satellite.timeline is None or not isinstance(satellite.timeline, datetime):
            raise ValueError("Every satellite must have a timeline")

        if satellite.velocity is None or not isinstance(satellite.velocity, (int, float)):
            raise ValueError("Every satellite must have a velocity")

        if satellite.visibility is None or not isinstance(satellite.visibility, str):
            raise ValueError("Every satellite must have a visibility")

        if satellite.visibility not in ("daylight", "eclipsed"):
            raise ValueError("Visibility must be either 'daylight' or 'eclipsed'")

        if satellite.location is None or not isinstance(satellite.location, str):
            raise ValueError("Every satellite must have a location")

        if not -90 <= satellite.latitude <= 90:
            raise ValueError("Every satellite must be between -90 and 90 degrees")

        if not -180 <= satellite.longitude <= 180:
            raise ValueError("Every satellite must be between -180 and 180 degrees")

        if satellite.altitude_in_km < 0:
            raise ValueError("Altitude cannot be negative")

    return satellites