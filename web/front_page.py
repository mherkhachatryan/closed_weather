import streamlit as st

st.title('Closed Weather')

st.header("Please enter your coordinates")

longitude = st.number_input('long', value=-0.1)
latitude = st.number_input('lat',value=-0.1)
#print(longitude, latitude)
if (longitude == True) and (latitude == True):
    st.text("We are showing requested data")
#st.text("We are showing requested data")
#st.balloons()
#print(longitude, latitude)