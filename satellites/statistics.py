from satellites.analysis import average_altitude, highest_altitude, lowest_altitude, average_velocity, \
    most_satellite_observations, average_time_between_observations, average_movement_per_observation
from satellites.search import search_by_name


def get_statistics(satellites, name):
    satellite_observations = search_by_name(satellites, name)

    return {
        "general": {
            "total_observations": len(satellites),
            "unique_satellites": len(set(satellite.norad_id for satellite in satellites)),
            "most_observations": most_satellite_observations(satellites),
        },

        "satellite": {
            "name": name,
            "observations": len(satellite_observations),
            "average_altitude": average_altitude(satellite_observations),
            "highest_altitude": highest_altitude(satellite_observations),
            "lowest_altitude": lowest_altitude(satellite_observations),
            "average_velocity": average_velocity(satellite_observations),
            "average_interval": average_time_between_observations(satellites, name),
            "average_movement": average_movement_per_observation(satellites, name)
        }
    }