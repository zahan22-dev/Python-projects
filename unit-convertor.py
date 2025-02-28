import streamlit as st
import os
from io import BytesIO
# App Title
st.title("🔄 Unit Converter")
st.subheader("Convert Length, Weight, and Temperature")

# Conversion Options
conversion_type = st.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])

# Length Conversion
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Weight Conversion
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Temperature Conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return ((value - 273.15) * 9/5) + 32

# User Input
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
