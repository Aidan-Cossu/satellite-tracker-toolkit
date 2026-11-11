
from satellites.loader.database_loader import load_database
from satellites.loader.external_importer import import_csv
from satellites.validation import validate_satellites

from menus import (
    statistics_menu,
    search_menu,
    analysis_menu,
    plot_altitude,
    plot_velocity,
    plot_movement,
    export_menu
)


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

        try:
            satellites = import_csv(filename)
        except (FileNotFoundError, KeyError, ValueError) as e:
            print(f"Could not import CSV: {e}")
            return None

    else:
        print("Invalid option.")
        return None

    satellites = validate_satellites(satellites)

    if satellites is None:
        return None

    satellites_by_name = {}

    for satellite in satellites:
        if satellite.name not in satellites_by_name:
            satellites_by_name[satellite.name] = []

        satellites_by_name[satellite.name].append(satellite)

    for observations in satellites_by_name.values():
        observations.sort(key=lambda satellite: satellite.timeline)

    return satellites, satellites_by_name


def main():
    try:
        satellites, satellites_by_name = load_data()
    except (FileNotFoundError, KeyError, ValueError) as e:
        print(f"Could not load data: {e}")
        return

    if satellites is None:
        return

    options = {
        "1": statistics_menu,
        "2": search_menu,
        "3": analysis_menu,
        "4": plot_altitude,
        "5": plot_velocity,
        "6": plot_movement,
        "7": export_menu
    }

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
        print("┖───────────────────────────────┘")

        choice = input("Choose an option: ")

        if choice == "0":
            break

        action = options.get(choice)

        if action:
            action(satellites, satellites_by_name)
        else:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
