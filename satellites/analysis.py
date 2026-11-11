import math

from datetime import timedelta

def average_altitude(satellites):
    if not satellites:
        return None

    return sum(satellite.altitude_in_km for satellite in satellites) / len(satellites)


def highest_altitude(satellites):
    if not satellites:
        return None

    return max(satellite.altitude_in_km for satellite in satellites)


def lowest_altitude(satellites):
    if not satellites:
        return None

    return min(satellite.altitude_in_km for satellite in satellites)


def average_velocity(satellites):
    if not satellites:
        return None

    return sum(satellite.velocity for satellite in satellites) / len(satellites)


def satellite_altitude_fluctuation(observations):
    if not observations:
        return 0

    altitudes = [satellite.altitude_in_km for satellite in observations]

    return max(altitudes) - min(altitudes)


def most_satellite_observations(satellites):
    observations = {}

    for satellite in satellites:
        if satellite.name not in observations:
            observations[satellite.name] = 0

        observations[satellite.name] += 1

    if not observations:
        return None

    most_observed = max(observations, key=observations.get)

    return most_observed, observations[most_observed]


def observation_duration(observations):
    if not observations:
        return None

    earliest = min(satellite.timeline for satellite in observations)
    latest = max(satellite.timeline for satellite in observations)

    return latest - earliest


def duration_between_observations(observations):
    return observation_duration(observations)


def time_intervals_between_observations(observations):
    ordered_observations = sorted(observations, key=lambda satellite: satellite.timeline )

    durations = []

    for i in range(1, len(ordered_observations)):
        duration = (ordered_observations[i].timeline -ordered_observations[i - 1].timeline)

        durations.append(duration)

    return durations


def average_time_between_observations(observations):
    durations = time_intervals_between_observations(observations)

    if not durations:
        return timedelta(0)

    return sum(durations, timedelta(0)) / len(durations)


def minimum_time_between_observations(observations):
    durations = time_intervals_between_observations(observations)

    if not durations:
        return None

    return min(durations)


def maximum_time_between_observations(observations):
    durations = time_intervals_between_observations(observations)

    if not durations:
        return None

    return max(durations)


def geodetic_to_ecef(satellite):
    latitude = math.radians(satellite.latitude)
    longitude = math.radians(satellite.longitude)

    n = 6378.137 / math.sqrt(1 - 0.00669438 * math.sin(latitude) ** 2)

    x = ((n + satellite.altitude_in_km)* math.cos(latitude)* math.cos(longitude))

    y = ((n + satellite.altitude_in_km)* math.cos(latitude)* math.sin(longitude))

    z = ((n * (1 - 0.00669438) + satellite.altitude_in_km) * math.sin(latitude))

    return x, y, z


def distance_between_observations(first, second):
    first_x, first_y, first_z = geodetic_to_ecef(first)
    second_x, second_y, second_z = geodetic_to_ecef(second)

    distance = math.sqrt(
        (first_x - second_x) ** 2 + (first_y - second_y) ** 2 + (first_z - second_z) ** 2)

    return distance


def movements_between_observations(observations):
    ordered_observations = sorted(observations,key=lambda satellite: satellite.timeline)

    movements = []

    for i in range(1, len(ordered_observations)):
        movement = distance_between_observations(ordered_observations[i - 1],ordered_observations[i])

        movements.append(movement)

    return movements


def average_movement_per_observation(observations):
    movements = movements_between_observations(observations)

    if not movements:
        return None

    return sum(movements) / len(movements)


def minimum_movement_per_observation(observations):
    movements = movements_between_observations(observations)

    if not movements:
        return None

    return min(movements)


def maximum_movement_per_observation(observations):
    movements = movements_between_observations(observations)

    if not movements:
        return None

    return max(movements)


def detect_irregular_observations(observations, expected_interval, tolerance):
    durations = time_intervals_between_observations(observations)

    if not durations:
        return None

    irregular = []

    for duration in durations:
        if (duration < expected_interval - tolerance or duration > expected_interval + tolerance):
            irregular.append(duration)

    return irregular
