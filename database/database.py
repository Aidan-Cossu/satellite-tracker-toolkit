import os
import sqlite3
from contextlib import closing

DATABASE = "database/satellite-tracker.db"

def connect():
    if not os.path.exists(DATABASE):
        raise FileNotFoundError(f"Database file not found: {DATABASE}")

    return sqlite3.connect(DATABASE)

def get_satellites():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                SAT_ID,
                ID,
                NAME,
                LATITUDE,
                LONGITUDE,
                ALTITUDE_IN_KM,
                TIMELINE,
                VELOCITY,
                VISIBILITY,
                LOCATION
            FROM SATELLITE
        """)

        return cursor.fetchall()