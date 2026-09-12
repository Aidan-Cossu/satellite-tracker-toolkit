def search_by_sat_id(satellites, satellite_id):
    return [satellite for satellite in satellites if satellite_id == satellite.sat_id]

def search_by_norad_id(satellites, norad_id):
    return [satellite for satellite in satellites if norad_id == satellite.norad_id]

def search_by_name(satellites, name):
    return [satellite for satellite in satellites if name.lower() == satellite.name.lower()]
