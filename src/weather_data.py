# weather_data.py
import json
from utils import kelvin_to_celsius, timestamp_to_isoformat

def process_weather_data(weather_data):
    # Convert temperature values to Celsius
    weather_data['main']['temp'] = kelvin_to_celsius(weather_data['main']['temp'])
    weather_data['main']['feels_like'] = kelvin_to_celsius(weather_data['main']['feels_like'])
    weather_data['main']['temp_min'] = kelvin_to_celsius(weather_data['main']['temp_min'])
    weather_data['main']['temp_max'] = kelvin_to_celsius(weather_data['main']['temp_max'])

    # Convert sunrise and sunset timestamps to ISO formatted strings
    weather_data['sys']['sunrise'] = timestamp_to_isoformat(weather_data['sys']['sunrise'])
    weather_data['sys']['sunset'] = timestamp_to_isoformat(weather_data['sys']['sunset'])

    return weather_data

def save_to_json(data, filename, append=False):
    mode = 'a' if append else 'w'

    with open(filename, mode) as json_file:
        if append:
            json_file.write(',\n')

        json.dump(data, json_file, indent=2, default=str)
        print(f"Data saved to {filename}")
