import requests
import pandas as pd


def _get_weather_info_api(long, lat):
    """Download by API call"""
    wheather_json = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}'
                                 f'&timezone=GMT'
                                 f'&longitude={long}&daily=temperature_2m_max&'
                                 f'&daily=temperature_2m_min'
                                 f'&daily=sunrise'
                                 f'&daily=sunset').json()

    return wheather_json


def get_weather(long, lat):
    """Get 6 days weather by coordinates"""
    data = pd.DataFrame(_get_weather_info_api(long, lat))

    data_transformed = data.loc[["time", "temperature_2m_max", "temperature_2m_min",
                                 "sunrise", "sunset"], "daily"]

    data_transformed = data_transformed.apply(lambda x: pd.Series(x)).T

    return data_transformed


if __name__ == "__main__":
    print(get_weather(44.5152, 40.1872))
