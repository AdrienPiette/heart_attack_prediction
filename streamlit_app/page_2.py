import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the pre-trained model and encoder (adjust paths as needed)
model = pickle.load(open(r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Model_training\best_model.pkl', 'rb'))
encoder = pickle.load(open(r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Model_training\encoders.pkl', 'rb'))

# User input features
def user_input_features():
    # Collecting input from user
    age = st.slider('Age', 29, 77, 50)
    sex = st.selectbox('Sex', ['M', 'F'])
    cp = st.selectbox('Chest Pain Type', ['ASY', 'NAP', 'ATA', 'TYP'])
    trestbps = st.slider('Resting Blood Pressure', 94, 200, 120)
    chol = st.slider('Cholesterol', 126, 564, 250)
    fbs = st.selectbox('Fasting Blood Sugar', [0, 1])
    restecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
    thalach = st.slider('Max Heart Rate', 71, 202, 150)
    exang = st.selectbox('Exercise Induced Angina', ['Y', 'N'])
    oldpeak = st.slider('ST Depression', 0.0, 6.2, 3.0)
    slope = st.selectbox('Slope of Peak Exercise ST Segment', ['Up', 'Flat', 'Down'])

    # Mapping categorical features using LabelEncoder
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
    
    return input_df

# Main function to display the prediction page
def predict_heart_disease():
    # Input data collection
    input_df = user_input_features()

    # Display user input for review
    st.write("User Input Features:")
    st.write(input_df)

    # Add a button to trigger prediction
    if st.button('Predict'):
        # Model prediction
        prediction = model.predict(input_df)

        # Show prediction result
        if prediction[0] == 1:
            st.write("## Prediction: High Risk of Heart Disease 💔")
        else:
            st.write("## Prediction: Low Risk of Heart Disease 💪")

# To retain the feature values after prediction, use session state
if 'input_df' not in st.session_state:
    st.session_state['input_df'] = None

def retain_input_values():
    if st.session_state['input_df'] is not None:
        st.write("Retaining user inputs from the previous prediction:")
        st.write(st.session_state['input_df'])

# Call the function to display the prediction page
if st.button("Submit Input"):
    st.session_state['input_df'] = user_input_features()

# Display the retained values
retain_input_values()

predict_heart_disease()
