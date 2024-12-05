import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Configure the Streamlit page
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")

# Introduction
st.title("Heart Disease Risk Prediction")
st.markdown("""
### Welcome to the Heart Disease Risk Prediction Tool! ❤️  
This tool uses a machine learning model to assess the likelihood of heart disease based on your health data.  
Please provide the following details, and click **Predict** to see your results.  
**Disclaimer**: This is for informational purposes only and should not replace medical advice from a healthcare professional.
""")

# Load the pre-trained model and encoder (adjust paths as needed)
model = pickle.load(open(r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Model_training\best_model.pkl', 'rb'))
encoder = pickle.load(open(r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Model_training\encoders.pkl', 'rb'))

# Collect user input features
st.write("Enter Your Details")
age = st.slider('Age', 29, 77, 50)
sex = st.selectbox('Sex', ['M', 'F'])
cp = st.selectbox('Chest Pain Type', ['ASY', 'NAP', 'ATA', 'TYP'])
trestbps = st.slider('Resting Blood Pressure (mmHg)', 94, 200, 120)
chol = st.slider('Cholesterol (mg/dL)', 126, 564, 250)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL (1 = Yes, 0 = No)', [0, 1])
restecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
thalach = st.slider('Maximum Heart Rate Achieved', 71, 202, 150)
exang = st.selectbox('Exercise-Induced Angina', ['Y', 'N'])
oldpeak = st.slider('ST Depression Induced by Exercise', 0.0, 6.2, 3.0)
slope = st.selectbox('Slope of Peak Exercise ST Segment', ['Up', 'Flat', 'Down'])

# Prepare input data
input_data = {
    'Age': age,
    'Sex': sex,
    'ChestPainType': cp,
    'RestingBP': trestbps,
    'Cholesterol': chol,
    'FastingBS': fbs,
    'RestingECG': restecg,
    'MaxHR': thalach,
    'ExerciseAngina': exang,
    'Oldpeak': oldpeak,
    'ST_Slope': slope
}

# Convert input into a pandas DataFrame for processing
input_df = pd.DataFrame(input_data, index=[0])

# Encode categorical columns
for col in encoder.keys():
    input_df[col] = encoder[col].transform(input_df[col])

# Display user input for review
st.write("### Your Input Data:")
st.write(input_df)

# Add a button to trigger prediction
if st.button('Predict'):
    # Make prediction
    prediction = model.predict(input_df)

    # Display prediction result
    if prediction[0] == 1:
        st.markdown("## 🔴 Prediction: High Risk of Heart Disease 💔")
        st.markdown("It's recommended to consult a healthcare professional for a detailed evaluation.")
    else:
        st.markdown("## 🟢 Prediction: Low Risk of Heart Disease 💪")
        st.markdown("Keep up the good habits and maintain a healthy lifestyle!")
