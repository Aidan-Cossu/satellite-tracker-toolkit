from satellites.analysis import average_altitude, highest_altitude, lowest_altitude, average_velocity, \
    most_satellite_observations, average_time_between_observations, average_movement_per_observation

def get_statistics(satellites, name):
    return {
        "total_observations": len(satellites),
        "unique_satellites": len(set(satellite.norad_id for satellite in satellites)),
        "average_altitude": average_altitude(satellites),
        "highest_altitude": highest_altitude(satellites),
        "lowest_altitude": lowest_altitude(satellites),
        "average_velocity": average_velocity(satellites),
        "most_satellite_observations": most_satellite_observations(satellites),
        "average_observation_interval": average_time_between_observations(satellites, name),
        "average_movement": average_movement_per_observation(satellites, name),
    }