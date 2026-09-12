from datetime import timedelta

from export.exporter import export_satellite_records_csv, export_analysis_records_csv
from satellites.analysis import average_altitude, highest_altitude, lowest_altitude, average_velocity, \
    satellite_altitude_fluctuation, most_satellite_observations, observation_duration, duration_between_observations, \
    average_time_between_observations, minimum_time_between_observations, maximum_time_between_observations, \
    average_movement_per_observation, minimum_movement_per_observation, \
    maximum_movement_per_observation, detect_irregular_observations, distance_between_observations
from satellites.search import search_by_name, search_by_norad_id, search_by_sat_id
from satellites.statistics import get_statistics
from satellites.validation import clean_satellites, Satellite
from visualization.charts import plot_velocity_over_time, plot_altitude_over_time, plot_movement_over_time


def main():
    satellites = clean_satellites()

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

        user_satellite_input = int(input(""))
        satellite = search_by_norad_id(satellites, user_satellite_input)

        print(satellite)

    elif search_choice == "3":
        print("┍───────────────────────────────┑")
        print("│   Enter satID of satellite    │")
        print("┖───────────────────────────────┛")

        user_satellite_input = int(input(""))
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
        print(average_altitude(satellites))

    elif analysis_choice == "2":
        print(highest_altitude(satellites))

    elif analysis_choice == "3":
        print(lowest_altitude(satellites))

    elif analysis_choice == "4":
        print(average_velocity(satellites))

    elif analysis_choice == "5":
        name = get_satellite_name()

        print(satellite_altitude_fluctuation(satellites, name))

    elif analysis_choice == "6":
        print(most_satellite_observations(satellites))

    elif analysis_choice == "7":
        name = get_satellite_name()

        print(observation_duration(satellites, name))

    elif analysis_choice == "8":
        name = get_satellite_name()

        print(duration_between_observations(satellites, name))

    elif analysis_choice == "9":
        name = get_satellite_name()

        print(average_time_between_observations(satellites, name))

    elif analysis_choice == "10":
        name = get_satellite_name()

        print(minimum_time_between_observations(satellites, name))

    elif analysis_choice == "11":
        name = get_satellite_name()

        print(maximum_time_between_observations(satellites, name))

    elif analysis_choice == "12":
        print("┍───────────────────────────────┑")
        print("│    Enter name of satellite 1  │")
        print("┖───────────────────────────────┛")

        user_satellite_input1 = input("")
        satellite1_observations = search_by_name(satellites, user_satellite_input1)

        if not satellite1_observations:
            print("No observations found.")
            return

        for i, satellite in enumerate(satellite1_observations, start=1):
            print(f"{i}. {satellite.timeline}")

        print("┍───────────────────────────────┑")
        print("│    Enter observation number   │")
        print("┖───────────────────────────────┛")

        observation1 = int(input("")) - 1

        if observation1 < 0 or observation1 >= len(satellite1_observations):
            print("Invalid observation number.")
            return

        satellite1 = satellite1_observations[observation1]

        print("┍───────────────────────────────┑")
        print("│    Enter name of satellite 2  │")
        print("┖───────────────────────────────┛")

        user_satellite_input2 = input("")
        satellite2_observations = search_by_name(satellites, user_satellite_input2)

        if not satellite2_observations:
            print("No observations found.")
            return

        for i, satellite in enumerate(satellite2_observations, start=1):
            print(f"{i}. {satellite.timeline}")

        print("┍───────────────────────────────┑")
        print("│    Enter observation number   │")
        print("┖───────────────────────────────┛")

        observation2 = int(input("")) - 1

        if observation2 < 0 or observation2 >= len(satellite2_observations):
            print("Invalid observation number.")
            return

        satellite2 = satellite2_observations[observation2]

        result = distance_between_observations(satellite1, satellite2)

        print(result)

    elif analysis_choice == "13":
        name = get_satellite_name()

        print(average_movement_per_observation(satellites, name))

    elif analysis_choice == "14":
        name = get_satellite_name()

        print(minimum_movement_per_observation(satellites, name))

    elif analysis_choice == "15":
        name = get_satellite_name()

        print(maximum_movement_per_observation(satellites, name))

    elif analysis_choice == "16":
        name = get_satellite_name()

        print("┍───────────────────────────────┑")
        print("│   Expected interval (minutes) │")
        print("┖───────────────────────────────┛")

        expected_interval_input = float(input(""))

        print("┍───────────────────────────────┑")
        print("│   Enter tolerance (minutes)   │")
        print("┖───────────────────────────────┛")

        tolerance_input = float(input(""))

        expected_interval = timedelta(minutes=expected_interval_input)
        tolerance = timedelta(minutes=tolerance_input)

        print(detect_irregular_observations(satellites, name, expected_interval, tolerance))

    elif analysis_choice == "0":
        pass

def plot_velocity(satellites):
    name = get_satellite_name()

    plot_velocity_over_time(satellites, name)

def plot_altitude(satellites):
    name = get_satellite_name()

    plot_altitude_over_time(satellites, name)

def plot_movement(satellites):
    name = get_satellite_name()

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

def get_satellite_name():
    print("┍───────────────────────────────┑")
    print("│    Enter name of satellite    │")
    print("┖───────────────────────────────┛")

    return input("")

if __name__ == "__main__":
    main()



