def search_by_sat_id(satellites, satellite_id):
    return [satellite for satellite in satellites if satellite.sat_id == satellite_id]

def search_by_norad_id(satellites, norad_id):
    return [satellite for satellite in satellites if satellite.norad_id == norad_id]

def search_by_name(satellites, name):
    name = name.strip().lower()

    return [satellite for satellite in satellites if satellite.name.strip().lower() == name]
