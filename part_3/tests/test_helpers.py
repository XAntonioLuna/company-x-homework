import math
from datetime import datetime
from app.helpers import helpers

def test_feet_to_in():
    test_value = 8
    expected_value = 96
    assert helpers.feet_to_in(test_value) == expected_value

def test_calculate_bmi():
    test_weight = 110
    test_height = 6
    expected_value = 14.92
    assert helpers.calculate_bmi(test_weight, test_height) == expected_value

def test_convert_string_to_datetime():
    test_value = '08/15/2021'
    expected_value = datetime(2021, 8, 15)
    assert helpers.convert_string_to_datetime(test_value) == expected_value
