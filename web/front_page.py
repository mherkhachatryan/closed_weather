import streamlit as st

import sys

sys.path.append("../closed_weather/")
from closed_weather.weather import get_weather

st.title('Closed Weather')

st.header("Please enter your coordinates")

longitude = st.number_input('long', value=-0.1)
latitude = st.number_input('lat', value=-0.1)

if longitude >= 0 and latitude >= 0:
    weather = get_weather(longitude, latitude)

    st.dataframe(weather)

