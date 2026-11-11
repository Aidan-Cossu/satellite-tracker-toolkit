from datetime import timedelta
from export.exporter import (export_satellite_records_csv,export_analysis_records_csv)
from satellites.analysis import (average_altitude,highest_altitude,lowest_altitude,average_velocity,satellite_altitude_fluctuation,most_satellite_observations,observation_duration,duration_between_observations,average_time_between_observations,minimum_time_between_observations,maximum_time_between_observations,average_movement_per_observation,minimum_movement_per_observation,maximum_movement_per_observation,detect_irregular_observations,distance_between_observations)
from satellites.search import (search_by_norad_id,search_by_sat_id)
from satellites.statistics import get_statistics
from visualization.charts import (plot_velocity_over_time,plot_altitude_over_time,plot_movement_over_time)

from utils.helpers import format_duration

def statistics_menu(satellites, satellites_by_name):
    name = get_satellite_name(satellites_by_name)
    statistics = get_statistics(satellites, satellites_by_name, name)

    general = statistics["general"]
    satellite = statistics["satellite"]

    print()
    print("┍────────────────────────────────────────┑")
    print("│           General Statistics           │")
    print("┖────────────────────────────────────────┛")
    print()

    print(f"Total observations:            {general['total_observations']}")
    print(f"Unique satellites:             {general['unique_satellites']}")

    most_name, most_count = general["most_observations"]
    print(f"Most observations:             {most_name} ({most_count})")

    print()
    print(f"┍{len(satellite['name']) * '─'}────────────────────────────────────────┑")
    print(f"│       {satellite['name']} Statistics         │")
    print(f"┖{len(satellite['name']) * '─'}────────────────────────────────────────┛")
    print()

    print(f"Observations:                 {satellite['observations']}")
    print(f"Average altitude:             {satellite['average_altitude']:.2f} km")
    print(f"Highest altitude:             {satellite['highest_altitude']:.2f} km")
    print(f"Lowest altitude:              {satellite['lowest_altitude']:.2f} km")
    print(f"Average velocity:             {satellite['average_velocity']:.2f} km/s")
    print(f"Average observation interval: {format_duration(satellite['average_interval'])}")
    print(f"Average movement:             {satellite['average_movement']:.2f} km")

def search_menu(satellites, satellites_by_name):
    print("┍────────────────────────────────────┑")
    print("│  1. Search by name of satellite    │")
    print("│  2. Search by noradID of satellite │")
    print("│  3. Search by satID of satellite   │")
    print("┖────────────────────────────────────┛")

    search_choice = input("Choose an option: ")

    if search_choice == "1":
        name = get_satellite_name(satellites_by_name)

        result = satellites_by_name[name]
        display_search_results(result)

    elif search_choice == "2":
        try:
            user_satellite_input = int(input("Enter noradID of satellite: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        result = search_by_norad_id(satellites, user_satellite_input)
        display_search_results(result)

    elif search_choice == "3":
        try:
            user_satellite_input = int(input("Enter satID of satellite: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        result = search_by_sat_id(satellites, user_satellite_input)
        display_search_results(result)

    else:
        print("Invalid input. Please enter a number.")


def display_search_results(satellites):
    if not satellites:
        print()
        print("No matching satellites found.")
        return

    print()
    print("┍────────────────────────────────────────┑")
    print("│              Search Results            │")
    print("┖────────────────────────────────────────┛")
    print()

    print(f"Found {len(satellites)} observations.")
    print()

    results_to_show = satellites[:10]

    for index, satellite in enumerate(results_to_show, start=1):
        print(f"{index}. {satellite.name}")
        print(f"   NORAD ID:   {satellite.norad_id}")
        print(f"   Satellite ID: {satellite.sat_id}")
        print(f"   Time:       {satellite.timeline}")
        print(f"   Latitude:   {satellite.latitude:.2f}°")
        print(f"   Longitude:  {satellite.longitude:.2f}°")
        print(f"   Altitude:   {satellite.altitude_in_km:.2f} km")
        print()

    if len(satellites) > 10:
        print(f"Showing 10 of {len(satellites)} observations.")

def analysis_menu(satellites, satellites_by_name):
    print("┍───────────────────────────────────────────────────┑")
    print("│        1. Average altitude                        │")
    print("│        2. Highest altitude                        │")
    print("│        3. Lowest altitude                         │")
    print("│        4. Average velocity                        │")
    print("│        5. Satellite altitude fluctuation          │")
    print("│        6. Most satellite observations             │")
    print("│        7. Observation duration                    │")
    print("│        8. Duration between observations           │")
    print("│        9. Average time between observations       │")
    print("│       10. Minimum time between observations       │")
    print("│       11. Maximum time between observations       │")
    print("│       12. Distance between observations           │")
    print("│       13. Average movement per observation        │")
    print("│       14. Minimum movement per observation        │")
    print("│       15. Maximum movement per observation        │")
    print("│       16. Detect irregular observations           │")
    print("│        0. Go back                                 │")
    print("┖───────────────────────────────────────────────────┛")

    options = {
        "1": lambda: average_altitude_menu(satellites),
        "2": lambda: highest_altitude_menu(satellites),
        "3": lambda: lowest_altitude_menu(satellites),
        "4": lambda: average_velocity_menu(satellites),
        "5": lambda: altitude_fluctuation_menu(satellites_by_name),
        "6": lambda: most_observations_menu(satellites),
        "7": lambda: observation_duration_menu(satellites_by_name),
        "8": lambda: duration_between_menu(satellites_by_name),
        "9": lambda: average_time_menu(satellites_by_name),
        "10": lambda: minimum_time_menu(satellites_by_name),
        "11": lambda: maximum_time_menu(satellites_by_name),
        "12": lambda: distance_between_menu(satellites_by_name),
        "13": lambda: average_movement_menu(satellites_by_name),
        "14": lambda: minimum_movement_menu(satellites_by_name),
        "15": lambda: maximum_movement_menu(satellites_by_name),
        "16": lambda: irregular_observations_menu(satellites_by_name)
    }

    choice = input("Choose an option: ")

    if choice == "0":
        return

    action = options.get(choice)

    if action:
        action()
    else:
        print("Invalid input. Please enter a number.")

def average_altitude_menu(satellites):
    print("┍────────────────────────┑")
    print("│    Average Altitude    │")
    print("┖────────────────────────┛")

    print(f"Average altitude across all satellites: {round(average_altitude(satellites), 3)} km")


def highest_altitude_menu(satellites):
    print("┍────────────────────────┑")
    print("│    Highest Altitude    │")
    print("┖────────────────────────┛")

    print(f"Highest altitude across all satellites: {round(highest_altitude(satellites), 3)} km")


def lowest_altitude_menu(satellites):
    print("┍────────────────────────┑")
    print("│     Lowest Altitude    │")
    print("┖────────────────────────┛")

    print(f"Lowest altitude across all satellites: {round(lowest_altitude(satellites), 3)} km")


def average_velocity_menu(satellites):
    print("┍────────────────────────┑")
    print("│    Average Velocity    │")
    print("┖────────────────────────┛")

    print(f"Average velocity across all satellites: {round(average_velocity(satellites), 3)} km/s")


def altitude_fluctuation_menu(satellites_by_name):
    print("┍────────────────────────────┑")
    print("│    Altitude Fluctuation    │")
    print("┖────────────────────────────┛")

    name = get_satellite_name(satellites_by_name)
    observations = satellites_by_name[name]

    print(f"Altitude fluctuation: {round(satellite_altitude_fluctuation(observations), 3)} km")


def most_observations_menu(satellites):
    print("┍───────────────────────────────────┑")
    print("│    Most Satellite Observations    │")
    print("┖───────────────────────────────────┛")

    most_observed, observation_count = most_satellite_observations(satellites)

    print(f"Satellite: {most_observed}")
    print(f"Observations: {observation_count}")


def observation_duration_menu(satellites_by_name):
    print("┍────────────────────────────┑")
    print("│    Observation Duration    │")
    print("┖────────────────────────────┛")

    name = get_satellite_name(satellites_by_name)
    duration = observation_duration(satellites_by_name[name])

    print(f"Observation duration: {format_duration(duration)}")


def duration_between_menu(satellites_by_name):
    print("┍──────────────────────────────────────┑")
    print("│     Duration Between Observations    │")
    print("┖──────────────────────────────────────┛")

    name = get_satellite_name(satellites_by_name)
    duration = duration_between_observations(satellites_by_name[name])

    print(f"Duration between observations: {format_duration(duration)}")


def average_time_menu(satellites_by_name):
    print("┍─────────────────────────────────────────┑")
    print("│    Average Time Between Observations    │")
    print("┖─────────────────────────────────────────┛")

    name = get_satellite_name(satellites_by_name)
    average_time = average_time_between_observations(satellites_by_name[name])

    print(f"Average time between observations: {format_duration(average_time)}")


def minimum_time_menu(satellites_by_name):
    print("┍─────────────────────────────────────────┑")
    print("│    Minimum Time Between Observations    │")
    print("┖─────────────────────────────────────────┛")

    name = get_satellite_name(satellites_by_name)
    minimum_time = minimum_time_between_observations(satellites_by_name[name])

    print(f"Minimum time between observations: {format_duration(minimum_time)}")


def maximum_time_menu(satellites_by_name):
    print("┍─────────────────────────────────────────┑")
    print("│    Maximum Time Between Observations    │")
    print("┖─────────────────────────────────────────┛")

    name = get_satellite_name(satellites_by_name)
    maximum_time = maximum_time_between_observations(satellites_by_name[name])

    print(f"Maximum time between observations: {format_duration(maximum_time)}")

def select_observation(satellites_by_name):
    name = get_satellite_name(satellites_by_name)
    observations = satellites_by_name[name]

    print("┍────────────────────────────┑")
    print("│     Satellite Timeline     │")
    print("┖────────────────────────────┛")

    for i, satellite in enumerate(observations, start=1):
        print(f"{i}. {satellite.timeline}")

    try:
        observation = int(input("Enter observation number: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    if observation < 0 or observation >= len(observations):
        print("Invalid observation number.")
        return None

    return observations[observation]


def distance_between_menu(satellites_by_name):
    satellite1 = select_observation(satellites_by_name)

    if satellite1 is None:
        return

    satellite2 = select_observation(satellites_by_name)

    if satellite2 is None:
        return

    result = distance_between_observations(satellite1, satellite2)

    print(f"Distance between observations: {result} km")

def average_movement_menu(satellites_by_name):
    print("┍──────────────────────────────────────────┑")
    print("│     Average Movement Per Observation     │")
    print("┖──────────────────────────────────────────┛")

    name = get_satellite_name(satellites_by_name)
    movement = average_movement_per_observation(satellites_by_name[name])

    if movement is None:
        print("No movement data available.")
        return

    print(f"Average movement per observation: {round(movement, 3)} km")


def minimum_movement_menu(satellites_by_name):
    print("┍──────────────────────────────────────────┑")
    print("│     Minimum Movement Per Observation     │")
    print("┖──────────────────────────────────────────┛")

    name = get_satellite_name(satellites_by_name)
    movement = minimum_movement_per_observation(satellites_by_name[name])

    if movement is None:
        print("No movement data available.")
        return

    print(f"Minimum movement per observation: {round(movement, 3)} km")


def maximum_movement_menu(satellites_by_name):
    print("┍──────────────────────────────────────────┑")
    print("│     Maximum Movement Per Observation     │")
    print("┖──────────────────────────────────────────┛")

    name = get_satellite_name(satellites_by_name)
    movement = maximum_movement_per_observation(satellites_by_name[name])

    if movement is None:
        print("No movement data available.")
        return

    print(f"Maximum movement per observation: {round(movement, 3)} km")

def irregular_observations_menu(satellites_by_name):
    name = get_satellite_name(satellites_by_name)

    print("┍───────────────────────────────┑")
    print("│   Expected interval (minutes) │")
    print("┖───────────────────────────────┛")

    try:
        expected_interval_input = float(input(""))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print("┍───────────────────────────────┑")
    print("│   Enter tolerance (minutes)   │")
    print("┖───────────────────────────────┛")

    try:
        tolerance_input = float(input(""))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    expected_interval = timedelta(minutes=expected_interval_input)
    tolerance = timedelta(minutes=tolerance_input)

    irregular = detect_irregular_observations(
        satellites_by_name[name],
        expected_interval,
        tolerance
    )

    if not irregular:
        print("No irregular observations detected.")
    else:
        print(f"{len(irregular)} irregular observations detected.")

        for i, duration in enumerate(irregular, start=1):
            print(f"{i}. {format_duration(duration)}")

def plot_velocity(satellites, satellites_by_name):
    name = get_satellite_name(satellites_by_name)
    plot_velocity_over_time(satellites, name)


def plot_altitude(satellites, satellites_by_name):
    name = get_satellite_name(satellites_by_name)
    plot_altitude_over_time(satellites, name)


def plot_movement(satellites, satellites_by_name):
    name = get_satellite_name(satellites_by_name)
    plot_movement_over_time(satellites, name)


def export_menu(satellites, satellites_by_name):
    print("┍────────────────────────────────────┑")
    print("│     1. Export satellite records    │")
    print("│     2. Export analysis records     │")
    print("│     0. Go back                     │")
    print("┖────────────────────────────────────┛")

    export_choice = input("Choose an option: ")

    if export_choice == "1":
        filename_records = input("Enter filename of records: ")

        return export_satellite_records_csv(
            satellites,
            filename_records
        )

    elif export_choice == "2":
        name = get_satellite_name(satellites_by_name)
        filename_analysis = input("Enter filename of records: ")

        return export_analysis_records_csv(
            satellites,
            satellites_by_name,
            name,
            filename_analysis
        )

    elif export_choice == "0":
        return

    else:
        print("Invalid input. Please enter a number.")

def get_satellite_name(satellites_by_name):
    names = sorted(satellites_by_name.keys())

    print("┍───────────────────────────────┑")
    print("│      Available satellites     │")
    print("┖───────────────────────────────┛")

    for name in names:
        print(f"  - {name}")

    print()
    print("┍───────────────────────────────┑")
    print("│    Enter name of satellite    │")
    print("┖───────────────────────────────┛")

    while True:
        name = input("").strip()

        for satellite_name in names:
            if satellite_name.lower() == name.lower():
                return satellite_name

        print("Satellite not found. Try again.")
