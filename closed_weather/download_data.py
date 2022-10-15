import requests
import pandas as pd


def get_weather_info(long, lat):
    wheather_json = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}'
                                 f'&timezone=GMT'
                                 f'&longitude={long}&daily=temperature_2m_max&'
                                 f'&daily=temperature_2m_min'
                                 f'&daily=sunrise'
                                 f'&daily=sunset').json()

    data = pd.DataFrame(wheather_json)

    data_transformed = data.loc[["time", "temperature_2m_max", "temperature_2m_min",
                                 "sunrise", "sunset"], "daily"]

    data_transformed = data_transformed.apply(lambda x: pd.Series(x)).T

    return data_transformed


data = get_weather_info(44.3, 42)
print(data)
