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
def get_interpretation(r_result):
    if r_result >= 90:
        return "Great Quality", "green"
    elif r_result >= 70:
        return "Good Quality", "orange"
    else:
        return "Bad Quality", "red"

if st.button("Predict Quality"):
    result = model.predict(Qualities)
    r_result = round(result[0], 2)
    interpretation, color = get_interpretation(r_result)
    st.success(f"Predicted Quality Rating: {r_result}")
    st.markdown(f"<span style='color:{color}; font-weight:bold;'>Status: {interpretation}</span>",unsafe_allow_html=True)
    progress_value = min(max(r_result / 100, 0), 1) 
    st.progress(progress_value)
    
    
