from datetime import timedelta

from export.exporter import export_satellite_records_csv, export_analysis_records_csv
from satellites.analysis import average_altitude, highest_altitude, lowest_altitude, average_velocity, \
    satellite_altitude_fluctuation, most_satellite_observations, observation_duration, duration_between_observations, \
    average_time_between_observations, minimum_time_between_observations, maximum_time_between_observations, \
    average_movement_per_observation, minimum_movement_per_observation, \
    maximum_movement_per_observation, detect_irregular_observations, distance_between_observations
from satellites.search import search_by_name, search_by_norad_id, search_by_sat_id
from satellites.statistics import get_statistics
from visualization.charts import plot_velocity_over_time, plot_altitude_over_time, plot_movement_over_time
from satellites.loader.database_loader import load_database
from satellites.loader.external_importer import import_csv
from satellites.validation import validate_satellites
from utils.helpers import format_duration

def load_data():
    print("┍─────────────────────────────────────────┑")
    print("│       Select data source:               │")
    print("│                                         │")
    print("│       1. Satellite Tracker database     │")
    print("│       2. Import external CSV data       │")
    print("└─────────────────────────────────────────┘")


    choice = input("Choose an option: ")

    if choice == "1":
        satellites = load_database()

    elif choice == "2":
        filename = input("Enter CSV filename: ")
        satellites = import_csv(filename)

    else:
        print("Invalid option.")
        return None

    return validate_satellites(satellites)

def main():
    satellites = load_data()

    if satellites is None:
        return

    while True:

        print("┍───────────────────────────────┑")
        print("│       Satellite Toolkit       │")
        print("│                               │")
        print("│       1. View statistics      │")
        print("│       2. Search satellite     │")
        print("│       3. Analyse satellite    │")
        print("│       4. Plot altitude        │")
        print("│       5. Plot velocity        │")
        print("│       6. Plot movement        │")
        print("│       7. Export data          │")
        print("│       0. Exit                 │")
        print("┖───────────────────────────────┛")

        choice = input("Choose an option: ")

        if choice == "1":
            statistics_menu(satellites)

        elif choice == "2":
            search_menu(satellites)

        elif choice == "3":
            analysis_menu(satellites)

        elif choice == "4":
            plot_altitude(satellites)

        elif choice == "5":
            plot_velocity(satellites)

        elif choice == "6":
            plot_movement(satellites)

        elif choice == "7":
            export_menu(satellites)

        elif choice == "0":
            break

def statistics_menu(satellites):
    print("┍───────────────────────────────┑")
    print("│    Enter name of satellite    │")
    print("┖───────────────────────────────┛")

    user_satellite_input = input("")
    statistics = get_statistics(satellites, user_satellite_input)

    print(statistics)

def search_menu(satellites):
    print("┍────────────────────────────────────┑")
    print("│  1. Search by name of satellite    │")
    print("│  2. Search by noradID of satellite │")
    print("│  3. Search by satID of satellite   │")
    print("┖────────────────────────────────────┛")

    search_choice = input("")

    if search_choice == "1":
        print("┍───────────────────────────────┑")
        print("│    Enter name of satellite    │")
        print("┖───────────────────────────────┛")

        user_satellite_input = input("")
        satellite = search_by_name(satellites, user_satellite_input)

        print(satellite)

    elif search_choice == "2":
        print("┍───────────────────────────────┑")
        print("│  Enter noradID of satellite   │")
        print("┖───────────────────────────────┛")

        try:
            user_satellite_input = int(input(""))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        satellite = search_by_norad_id(satellites, user_satellite_input)

        print(satellite)

    elif search_choice == "3":
        print("┍───────────────────────────────┑")
        print("│   Enter satID of satellite    │")
        print("┖───────────────────────────────┛")

        try:
            user_satellite_input = int(input(""))
        except ValueError:
            print("invalid input. Please enter a number.")
            return

        satellite = search_by_sat_id(satellites, user_satellite_input)

        print(satellite)

def analysis_menu(satellites):
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

    analysis_choice = input("Choose an option: ")

    if analysis_choice == "1":
        print("┍────────────────────────┑")
        print("│    Average Altitude    │")
        print("┖────────────────────────┛")

        print(f"Average altitude: {round(average_altitude(satellites), 3)} km")

    elif analysis_choice == "2":
        print("┍────────────────────────┑")
        print("│    Highest Altitude    │")
        print("┖────────────────────────┛")

        print(f"Highest altitude: {round(highest_altitude(satellites), 3)} km")

    elif analysis_choice == "3":
        print("┍────────────────────────┑")
        print("│     Lowest Altitude    │")
        print("┖────────────────────────┛")

        print(f"Lowest altitude: {round(lowest_altitude(satellites), 3)} km")

    elif analysis_choice == "4":
        print("┍────────────────────────┑")
        print("│    Average Velocity    │")
        print("┖────────────────────────┛")

        print(f"Average velocity: {round(average_velocity(satellites), 3)} km/s")

    elif analysis_choice == "5":
        print("┍────────────────────────────┑")
        print("│    Altitude Fluctuation    │")
        print("┖────────────────────────────┛")

        name = get_satellite_name(satellites)

        print(f"Altitude fluctuation: {round(satellite_altitude_fluctuation(satellites, name), 3)}")

    elif analysis_choice == "6":
        print("┍───────────────────────────────────┑")
        print("│    Most Satellite Observations    │")
        print("┖───────────────────────────────────┛")

        most_observed, observation_count = most_satellite_observations(satellites)

        print(f"Satellite: {most_observed}")
        print(f"Observations: {observation_count}")

    elif analysis_choice == "7":
        print("┍────────────────────────────┑")
        print("│    Observation Duration    │")
        print("┖────────────────────────────┛")

        name = get_satellite_name(satellites)
        duration = observation_duration(satellites, name)

        print(f"Observation duration: {format_duration(duration)}")

    elif analysis_choice == "8":
        print("┍──────────────────────────────────────┑")
        print("│     Duration Between Observations    │")
        print("┖──────────────────────────────────────┛")

        name = get_satellite_name(satellites)

        print(f"Duration between observations: {duration_between_observations(satellites, name)}")

    elif analysis_choice == "9":
        print("┍─────────────────────────────────────────┑")
        print("│    Average Time Between Observations    │")
        print("┖─────────────────────────────────────────┛")

        name = get_satellite_name(satellites)
        average_time = average_time_between_observations(satellites, name)

        print(f"Average time between observations: {format_duration(average_time)}")

    elif analysis_choice == "10":
        print("┍─────────────────────────────────────────┑")
        print("│    Minimum Time Between Observations    │")
        print("┖─────────────────────────────────────────┛")

        name = get_satellite_name(satellites)
        minimum_time = minimum_time_between_observations(satellites, name)

        print(f"Minimum time between observations: {format_duration(minimum_time)}")

    elif analysis_choice == "11":
        print("┍─────────────────────────────────────────┑")
        print("│    Maximum Time Between Observations    │")
        print("┖─────────────────────────────────────────┛")

        name = get_satellite_name(satellites)
        maximum_time = maximum_time_between_observations(satellites, name)

        print(f"Maximum time between observations: {format_duration(maximum_time)}")

    elif analysis_choice == "12":
        print("┍───────────────────────────────┑")
        print("│    Enter name of satellite 1  │")
        print("┖───────────────────────────────┛")

        user_satellite_input1 = get_satellite_name(satellites)
        satellite1_observations = search_by_name(satellites, user_satellite_input1)

        if not satellite1_observations:
            print("No observations found.")
            return

        print("┍────────────────────────────┑")
        print("│     Satellite Timeline     │")
        print("┖────────────────────────────┛")

        for i, satellite in enumerate(satellite1_observations, start=1):
            print(f"{i}. {satellite.timeline}")

        print("┍───────────────────────────────┑")
        print("│    Enter observation number   │")
        print("┖───────────────────────────────┛")

        try:
            observation1 = int(input("")) - 1
        except ValueError:
            print("Invalid input. Please enter a number")
            return

        if observation1 < 0 or observation1 >= len(satellite1_observations):
            print("Invalid observation number.")
            return

        satellite1 = satellite1_observations[observation1]

        print("┍───────────────────────────────┑")
        print("│    Enter name of satellite 2  │")
        print("┖───────────────────────────────┛")

        user_satellite_input2 = get_satellite_name(satellites)
        satellite2_observations = search_by_name(satellites, user_satellite_input2)

        if not satellite2_observations:
            print("No observations found.")
            return

        print("┍────────────────────────────┑")
        print("│     Satellite Timeline     │")
        print("┖────────────────────────────┛")

        for i, satellite in enumerate(satellite2_observations, start=1):
            print(f"{i}. {satellite.timeline}")

        print("┍───────────────────────────────┑")
        print("│    Enter observation number   │")
        print("┖───────────────────────────────┛")

        try:
            observation2 = int(input("")) - 1
        except ValueError:
            print("Invalid input. Please enter a number")
            return

        if observation2 < 0 or observation2 >= len(satellite2_observations):
            print("Invalid observation number.")
            return

        satellite2 = satellite2_observations[observation2]

        result = distance_between_observations(satellite1, satellite2)

        print(result)

    elif analysis_choice == "13":
        print("┍──────────────────────────────────────────┑")
        print("│     Average Movement Per Observation     │")
        print("┖──────────────────────────────────────────┛")

        name = get_satellite_name(satellites)

        print(f"Average movement per observation: {round(average_movement_per_observation(satellites, name), 3)} km")

    elif analysis_choice == "14":
        print("┍──────────────────────────────────────────┑")
        print("│     Minimum Movement Per Observation     │")
        print("┖──────────────────────────────────────────┛")

        name = get_satellite_name(satellites)

        print(f"Minimum movement per observation: {round(minimum_movement_per_observation(satellites, name), 3)} km")

    elif analysis_choice == "15":
        print("┍──────────────────────────────────────────┑")
        print("│     Maximum Movement Per Observation     │")
        print("┖──────────────────────────────────────────┛")

        name = get_satellite_name(satellites)

        print(f"Maximum movement per observation: {round(maximum_movement_per_observation(satellites, name), 3)} km")

    elif analysis_choice == "16":
        name = get_satellite_name(satellites)

        print("┍───────────────────────────────┑")
        print("│   Expected interval (minutes) │")
        print("┖───────────────────────────────┛")

        try:
            expected_interval_input = float(input(""))
        except ValueError:
            print("Invalid input. Please enter a number")
            return

        print("┍───────────────────────────────┑")
        print("│   Enter tolerance (minutes)   │")
        print("┖───────────────────────────────┛")

        try:
            tolerance_input = float(input(""))
        except ValueError:
            print("Invalid input. Please enter a number")
            return

        expected_interval = timedelta(minutes=expected_interval_input)
        tolerance = timedelta(minutes=tolerance_input)

        irregular = detect_irregular_observations(satellites, name, expected_interval, tolerance)

        if not irregular:
            print("No irregular observations detected.")
        else:
            print(f"{len(irregular)} irregular observations detected.")

            for i, duration in enumerate(irregular, start=1):
                print(f"{i}. {format_duration(duration)}")

    elif analysis_choice == "0":
        pass

def plot_velocity(satellites):
    name = get_satellite_name(satellites)

    plot_velocity_over_time(satellites, name)

def plot_altitude(satellites):
    name = get_satellite_name(satellites)

    plot_altitude_over_time(satellites, name)

def plot_movement(satellites):
    name = get_satellite_name(satellites)

    plot_movement_over_time(satellites, name)


def export_menu(satellites):
    print("┍────────────────────────────────────┑")
    print("│     1. Export satellite records    │")
    print("│     2. Export analysis records     │")
    print("│     0. Go back                     │")
    print("┖────────────────────────────────────┛")

    export_choice = input("")

    if export_choice == "1":
        filename_records = input("Enter filename of records: ")

        result = export_satellite_records_csv(satellites, filename_records)
        return result

    elif export_choice == "2":
        filename_analysis = input("Enter filename of records: ")

        result = export_analysis_records_csv(satellites, filename_analysis)
        return result

    elif export_choice == "0":
        pass

def get_satellite_name(satellites):
    names = sorted(set(satellite.name for satellite in satellites))

    print("┍───────────────────────────────┑")
    print("│      Available satellites     │")
    print("┖───────────────────────────────┛")

    for name in names:
        print(f"  - {name}")

    print()
    print("Enter name of satellite:")

    return input("").strip()

if __name__ == "__main__":
    main()