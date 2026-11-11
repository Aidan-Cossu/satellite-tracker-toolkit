import math
from datetime import datetime, timedelta

import pytest

from satellites.satellite import Satellite
from satellites.analysis import (geodetic_to_ecef,distance_between_observations)

def create_satellite(latitude,longitude,altitude=0.0,name="Test Satellite"):
    return Satellite(name=name,norad_id=12345,latitude=latitude,longitude=longitude,altitude_in_km=altitude,velocity=7.5,timeline=datetime(2026, 1, 1, 12, 0, 0))

def test_geodetic_to_ecef_equator():
    satellite = create_satellite(0, 0)

    x, y, z = geodetic_to_ecef(satellite)

    assert x == pytest.approx(6378.137)
    assert y == pytest.approx(0)
    assert z == pytest.approx(0)

def test_geodetic_to_ecef_quarter_equator():
    satellite = create_satellite(0, 90)

    x, y, z = geodetic_to_ecef(satellite)

    assert x == pytest.approx(0, abs=1e-9)
    assert y == pytest.approx(6378.137)
    assert z == pytest.approx(0)

def test_geodetic_to_ecef_north_pole():
    satellite = create_satellite(90, 0)

    x, y, z = geodetic_to_ecef(satellite)

    assert x == pytest.approx(0, abs=1e-9)
    assert y == pytest.approx(0, abs=1e-9)
    assert z == pytest.approx(6356.752314)

def test_geodetic_to_ecef_altitude():
    satellite = create_satellite(0, 0, altitude=400)

    x, y, z = geodetic_to_ecef(satellite)

    assert x == pytest.approx(6778.137)
    assert y == pytest.approx(0)
    assert z == pytest.approx(0)

def test_distance_between_identical_observations():
    satellite1 = create_satellite(0, 0)
    satellite2 = create_satellite(0, 0)

    distance = distance_between_observations(satellite1,satellite2)

    assert distance == pytest.approx(0)

def test_distance_between_equator_observations():
    satellite1 = create_satellite(0, 0)
    satellite2 = create_satellite(0, 90)

    distance = distance_between_observations(satellite1,satellite2)

    expected_distance = math.sqrt(2) * 6378.137

    assert distance == pytest.approx(expected_distance)

def test_distance_between_observations_with_altitude():
    satellite1 = create_satellite(0, 0, altitude=0)
    satellite2 = create_satellite(0, 0, altitude=400)

    distance = distance_between_observations(satellite1,satellite2)

    assert distance == pytest.approx(400)