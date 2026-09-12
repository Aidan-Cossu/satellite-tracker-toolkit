import sqlite3

DATABASE = "database/satellite-tracker.db"

def connect():
    return sqlite3.connect(DATABASE)

def get_satellites():
    connection = connect()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM SATELLITE")

    data = cursor.fetchall()

    connection.close()

    return data