import csv

def import_csv(filename):
    satellites = []

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            satellites.append(row)

    return satellites