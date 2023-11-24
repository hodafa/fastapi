# utils.py
import datetime

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def timestamp_to_isoformat(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).isoformat()

