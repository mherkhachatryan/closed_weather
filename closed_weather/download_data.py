import requests
import json


def get_weather_info(long, lat, save=True):
    wheather_json = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}'
                                 f'&timezone=GMT'
                                 f'&longitude={long}&daily=temperature_2m_max&'
                                 f'&daily=temperature_2m_min'
                                 f'&daily=sunrise'
                                 f'&daily=sunset').json()

    if save:
        with open('data.json', 'w') as json_file:
            json.dump(wheather_json, json_file)


get_weather_info(44.3, 42, save=True)
