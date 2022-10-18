import streamlit as st

st.title('Closed Weather')

st.header("Please enter your coordinates")

longitude = st.number_input('long', value=-0.1)
latitude = st.number_input('lat', value=-0.1)

if longitude >= 0 and latitude >= 0:
    st.text("We are showing requested data")
