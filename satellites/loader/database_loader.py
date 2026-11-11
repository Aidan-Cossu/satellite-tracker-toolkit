from datetime import datetime
from database.database import get_satellites as get_database_satellites
from satellites.satellite import Satellite

def load_database():
    rows = get_database_satellites()

    satellites = []

    for row in rows:
        satellite = Satellite(
            sat_id=row[0],
            norad_id=row[1],
            name=row[2],
            latitude=row[3],
            longitude=row[4],
            altitude_in_km=row[5],
            timeline=datetime.fromisoformat(row[6].split("[")[0]),
            velocity=row[7],
            visibility=row[8],
            location=row[9]
        )

        satellites.append(satellite)

    return satellites