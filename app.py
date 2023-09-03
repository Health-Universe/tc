import streamlit as st
from logging import getLogger
log = getLogger(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

st.title("Celsius to Fahrenheit Converter")

celsius = st.number_input("Enter temperature in Celsius:", value=0.0)

fahrenheit = celsius_to_fahrenheit(celsius)
print("test logging")
log.info("test logger")
st.write(f"{celsius:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
