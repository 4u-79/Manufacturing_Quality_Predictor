import streamlit as st
import pandas as pd
import joblib

model = joblib.load('models/manufacturing_model.pkl')

st.title("Manufacturing_Quality_Prediction")

temperature = st.number_input("Temperature (°C)")
pressure = st.number_input("Pressure (kPa)")
temp_pressure = temperature * pressure
fusion = st.number_input("Material Fusion Metric")
transformation = st.number_input("Material Transformation Metric")

Qualities = pd.DataFrame({
    "Temperature (°C)": [temperature],
    "Pressure (kPa)": [pressure],
    "Temperature x Pressure": [temp_pressure],
    "Material Fusion Metric": [fusion],
    "Material Transformation Metric": [transformation]

})

if st.button("Predict Quality"):
    result = model.predict(Qualities)
    st.success(f"Predicted Quality Rating: {result[0]}")