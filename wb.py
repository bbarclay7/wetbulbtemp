#!/bin/sh
# -*- coding: utf-8 ; mode: python -*-
"exec" "`dirname $0`/local/miniconda/envs/miniconda/bin/python3" "$0" "$@"

import math

def convert_to_wet_bulb(temperature_fahrenheit, relative_humidity):
    # Convert Fahrenheit to Celsius
    temperature_celsius = (temperature_fahrenheit - 32) * 5.0/9.0
    # Stull's formula
    wet_bulb_celsius = temperature_celsius * \
                       math.atan(0.151977 * (relative_humidity + 8.313659)**0.5) + \
                       math.atan(temperature_celsius + relative_humidity) - \
                       math.atan(relative_humidity - 1.676331) + \
                       0.00391838 * (relative_humidity)**1.5 * \
                       math.atan(0.023101 * relative_humidity) - 4.686035
    # Convert Celsius back to Fahrenheit
    wet_bulb_f = wet_bulb_celsius *9.0/5.0 + 32
    return wet_bulb_f


#print(convert_to_wet_bulb(98.49,27.4))

import streamlit as st

# Use streamlit functions to create a simple UI
st.title('Ambient to Wet-bulb Temperature Converter')

# User input
temperature_fahrenheit = st.number_input('Enter Temperature in Fahrenheit')
relative_humidity = st.number_input('Enter Relative Humidity in %')

# Call function and store result
if st.button('Calculate'):
    wet_bulb_fahrenheit = convert_to_wet_bulb(temperature_fahrenheit, relative_humidity)
    
    # Display the result
    st.write('The Wet-bulb temperature is: ', wet_bulb_fahrenheit, ' Fahrenheit')

#In this code, `st.number_input()` creates an input field where users can enter a number, and `st.write()` is used to display the result in the Streamlit web application. You would run this app from the command line with `streamlit run app.py` where `app.py` is the name of your python file.
