from datetime import datetime

def feet_to_in(feet: float) -> float:
    return feet * 12

def calculate_bmi(weight_lbs: float, height_feet: float) -> float:
    # Formula: weight (lb) / [height (in)]^2 x 703
    # rounded to two decimals
    height_in = feet_to_in(height_feet)
    return round((weight_lbs / pow(height_in, 2)) * 703, 2)

def convert_string_to_datetime(date: str) -> datetime:
    """
    Takes a string with format MM/DD/YYYY and returns a datetime object
    """
    month, day, year = date.split('/')
    return datetime(int(year), int(month), int(day))