import matplotlib.pyplot as plt

from satellites.analysis import average_movement_per_observation, distance_between_observations
from satellites.search import search_by_name


def plot_altitude_over_time(satellites, name):
    observations = search_by_name(satellites, name)

    observations.sort(key=lambda satellite: satellite.timeline)

    times = [satellite.timeline for satellite in observations]
    altitude = [satellite.altitude_in_km for satellite in observations]

    plt.plot(times, altitude)
    plt.xlabel("Time")
    plt.ylabel("Altitude (km)")
    plt.title(f"{name} altitude over time")
    plt.show()


def plot_velocity_over_time(satellites, name):
    observations = search_by_name(satellites, name)

    observations.sort(key=lambda satellite: satellite.timeline)

    times = [satellite.timeline for satellite in observations]
    velocity = [satellite.velocity for satellite in observations]

    plt.plot(times, velocity)
    plt.xlabel("Time")
    plt.ylabel("Velocity (km/s)")
    plt.title(f"{name} velocity over time")
    plt.show()

def plot_movement_over_time(satellites, name):
    observations = search_by_name(satellites, name)

    if len(observations) < 2:
        return None

    observations.sort(key=lambda satellite: satellite.timeline)

    times = []
    movements = []

    for i in range(1, len(observations)):
        movement = distance_between_observations(
            observations[i - 1],
            observations[i]
        )

        times.append(observations[i].timeline)
        movements.append(movement)

    plt.plot(times, movements)
    plt.xlabel("Time")
    plt.ylabel("Movement (km)")
    plt.title(f"{name} movement over time")
    plt.show()