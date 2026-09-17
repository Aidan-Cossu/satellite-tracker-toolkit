import csv
from satellites.statistics import get_statistics

def export_satellite_records_csv(satellites, filename):
    with open(filename, 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            "sat_id",
            "norad_id",
            "name",
            "latitude",
            "longitude",
            "altitude_in_km",
            "timeline",
            "velocity",
            "visibility",
            "location"
        ])

        for satellite in satellites:
            writer.writerow([
                satellite.sat_id,
                satellite.norad_id,
                satellite.name,
                satellite.latitude,
                satellite.longitude,
                satellite.altitude_in_km,
                satellite.timeline,
                satellite.velocity,
                satellite.visibility,
                satellite.location
            ])

def export_analysis_records_csv(satellites, name, filename):
    statistics = get_statistics(satellites, name)

    with open(filename, 'w', newline="", encoding="utf=8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            "total_observations",
            "unique_satellites",
            "average_altitude",
            "highest_altitude",
            "lowest_altitude",
            "average_velocity",
            "most_satellite_observations",
            "average_observation_interval",
            "average_movement"
        ])

        general = statistics["general"]
        satellite = statistics["satellite"]

        writer.writerow([
            general["total_observations"],
            general["unique_satellites"],
            general["most_observations"],
            satellite["average_altitude"],
            satellite["highest_altitude"],
            satellite["lowest_altitude"],
            satellite["average_velocity"],
            satellite["average_interval"],
            satellite["average_movement"]
        ])