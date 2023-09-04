import streamlit as st
import datetime
import sys
from logging import getLogger
log = getLogger(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

st.title("Celsius to Fahrenheit Converter")

celsius = st.number_input("Enter temperature in Celsius:", value=0.0)

fahrenheit = celsius_to_fahrenheit(celsius)
dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"test logging {dt}")
sys.stdout.flush()
log.info("test logger")
st.write(f"{celsius:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
