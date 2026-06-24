import streamlit as st
import pandas as pd
import joblib

# Load the trained model
lr = joblib.load('linear_regression_model.pkl')

st.title('Crop Production Prediction')
st.write('Enter the area in hectares to predict crop production.')

# Input for Area in hectares
area_input = st.number_input('Area in hectares', min_value=0.0, format="%.2f")

if st.button('Predict Production'):
    if area_input is not None:
        # Make prediction
        predicted_production = lr.predict([[area_input]])
        st.success(f'Predicted Production in tons: {predicted_production[0]:.2f}')
    else:
        st.warning('Please enter a valid area.')
