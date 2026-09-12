import math

from datetime import timedelta
from satellites.search import search_by_name

def average_altitude(satellites):
    return sum(satellite.altitude_in_km for satellite in satellites) / len(satellites)

def highest_altitude(satellites):
    return max(satellites, key=lambda satellite: satellite.altitude_in_km)

def lowest_altitude(satellites):
    return min(satellites, key=lambda satellite: satellite.altitude_in_km)

def average_velocity(satellites):
    return sum(satellite.velocity for satellite in satellites) / len(satellites)

def satellite_altitude_fluctuation(satellites, name):
    matching_satellites = search_by_name(satellites, name)

    if not matching_satellites:
        return None

    altitudes = [satellite.altitude_in_km for satellite in matching_satellites]

    return max(altitudes) - min(altitudes)

def most_satellite_observations(satellites):
    observations = {}

    for satellite in satellites:
        if satellite.name not in observations:
            observations[satellite.name] = 0
        observations[satellite.name] += 1

    most_observed = max(observations, key=observations.get)

    return most_observed, observations[most_observed]

def observation_duration(satellites, name):
    matching_satellites = search_by_name(satellites, name)

    if not matching_satellites:
        return None

    earliest = min(satellite.timeline for satellite in matching_satellites)
    latest =  max(satellite.timeline for satellite in matching_satellites)

    return latest - earliest

def duration_between_observations(satellites, name):
    observations = []

    matching_satellites = search_by_name(satellites, name)

    if not matching_satellites:
        return None

    matching_satellites.sort(key=lambda satellite: satellite.timeline)

    for i in range(1, len(matching_satellites)):
        duration = (matching_satellites[i].timeline - matching_satellites[i - 1].timeline)

        observations.append(duration)

    return observations

def average_time_between_observations(satellites, name):
    durations = duration_between_observations(satellites, name)

    if not durations:
        return None

    return sum(durations, timedelta()) / len(durations)

def minimum_time_between_observations(satellites, name):
    durations = duration_between_observations(satellites, name)

    if not durations:
        return None

    return min(durations)

def maximum_time_between_observations(satellites, name):
    durations = duration_between_observations(satellites, name)

    if not durations:
        return None

    return max(durations)

def geodetic_to_ecef(satellite):
    latitude = math.radians(satellite.latitude)
    longitude = math.radians(satellite.longitude)

    n = 6378.137 / math.sqrt(1 - 0.00669438 * math.sin(latitude)**2)

    x = (n + satellite.altitude_in_km) * math.cos(latitude) * math.cos(longitude)
    y = (n + satellite.altitude_in_km) * math.cos(latitude) * math.sin(longitude)
    z = (n * (1 - 0.00669438) + satellite.altitude_in_km) * math.sin(latitude)

    return x, y, z

def distance_between_observations(first, second):
    first_x, first_y, first_z = geodetic_to_ecef(first)
    second_x, second_y, second_z = geodetic_to_ecef(second)

    distance = math.sqrt((first_x - second_x) ** 2 + (first_y - second_y) ** 2 + (first_z - second_z) ** 2)

    return distance

def average_movement_per_observation(satellites, name):
    matching_satellites = search_by_name(satellites, name)

    if len(matching_satellites) < 2:
        return None

    matching_satellites.sort(key=lambda satellite: satellite.timeline)

    movements = []

    for i in range(1, len(matching_satellites)):
        movement = distance_between_observations(matching_satellites[i-1], matching_satellites[i])

        movements.append(movement)

    return sum(movements) / len(movements)

def minimum_movement_per_observation(satellites, name):
    matching_satellites = search_by_name(satellites, name)

    if len(matching_satellites) < 2:
        return None

    matching_satellites.sort(key=lambda satellite: satellite.timeline)

    movements = []

    for i in range(1, len(matching_satellites)):
        movement = distance_between_observations(matching_satellites[i-1], matching_satellites[i])

        movements.append(movement)

    return min(movements)

def maximum_movement_per_observation(satellites, name):
    matching_satellites = search_by_name(satellites, name)

    if len(matching_satellites) < 2:
        return None

    matching_satellites.sort(key=lambda satellite: satellite.timeline)

    movements = []

    for i in range(1, len(matching_satellites)):
        movement = distance_between_observations(matching_satellites[i-1], matching_satellites[i])

        movements.append(movement)

    return max(movements)

def detect_irregular_observations(satellites, name, expected_interval, tolerance):
    durations = duration_between_observations(satellites, name)

    if not durations:
        return None

    irregular = []

    for duration in durations:
        if duration < expected_interval - tolerance or duration > expected_interval + tolerance:
            irregular.append(duration)

    return irregular