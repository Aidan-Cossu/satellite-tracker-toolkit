import csv
from datetime import datetime

from satellites.satellite import Satellite

def import_csv(filename):
    satellites = []

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            satellite = Satellite(
                sat_id=int(row["sat_id"]),
                norad_id=int(row["norad_id"]),
                name=row["name"],
                latitude=float(row["latitude"]),
                longitude=float(row["longitude"]),
                altitude_in_km=float(row["altitude_in_km"]),
                timeline=datetime.fromisoformat(row["timeline"].split("[")[0]),
                velocity=float(row["velocity"]),
                visibility=row["visibility"],
                location=row["location"]
            )

            satellites.append(satellite)

    return satellites