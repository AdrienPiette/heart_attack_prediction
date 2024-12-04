import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model and encoder (adjust paths as needed)
model = pickle.load(open(r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Model_training\best_model.pkl', 'rb'))
encoder = pickle.load(open(r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Model_training\encoders.pkl', 'rb'))

# Page Title
st.title("Heart Disease Prediction")

# Collect user input
age = st.slider('Age', min_value=29, max_value=77, value=50)
sex = st.selectbox('Sex', options=['Male', 'Female'])
cp = st.selectbox('Chest Pain Type', options=['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
restecg = st.selectbox('Resting ECG', options=['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
exang = st.selectbox('Exercise Angina', options=['Yes', 'No'])
slope = st.selectbox('ST Slope', options=['Upsloping', 'Flat', 'Downsloping'])
chol = st.slider('Cholesterol', min_value=126, max_value=564, value=200)
fbs = st.selectbox('Fasting Blood Sugar', options=['Yes', 'No'])

# Encode categorical variables
sex = 1 if sex == 'Male' else 0
cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
cp = cp_mapping[cp]
restecg_mapping = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2}
restecg = restecg_mapping[restecg]
exang = 1 if exang == 'Yes' else 0
slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
slope = slope_mapping[slope]
fbs = 1 if fbs == 'Yes' else 0

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'Age': [age],
    'Sex': [sex],
    'ChestPainType': [cp],
    'RestingECG': [restecg],
    'ExerciseAngina': [exang],
    'ST_Slope': [slope],
    'Cholesterol': [chol],
    'FastingBS': [fbs]
})

# Apply the encoder to encode categorical features
input_encoded = encoder.transform(input_data)

# Make the prediction using the model
if st.button('Predict'):
    prediction = model.predict(input_encoded)

    # Display the result
    if prediction[0] == 1:
        st.error("The model predicts that you are at risk for heart disease.")
    else:
        st.success("The model predicts that you are not at risk for heart disease.")
