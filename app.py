

import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit App UI
def temperature_converter():
    st.title("Temperature Converter")

    # Select conversion type
    option = st.selectbox(
        "Choose the conversion type:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
    )

    # Based on the option selected
    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:")
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:")
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Run the Streamlit app
if __name__ == '__main__':
    temperature_converter()
