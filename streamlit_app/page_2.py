import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model and encoder (with caching)
@st.cache
def load_model():
    try:
        model = pickle.load(open(r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Model_training\best_model.pkl', 'rb'))
        encoder = pickle.load(open(r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Model_training\encoders.pkl', 'rb'))
        return model, encoder
    except Exception as e:
        st.error(f"Error loading model or encoder: {e}")
        return None, None

model, encoder = load_model()

# Check if model and encoder are loaded
if model is None or encoder is None:
    st.stop()

# Page Title
st.title("Heart Disease Prediction")

def user_input_features():
    try:
        # Collect numerical inputs
        age = st.slider('Age', 29, 77, 50)
        trestbps = st.slider('Resting Blood Pressure (mmHg)', 94, 200, 120)
        chol = st.slider('Cholesterol (mg/dL)', 126, 564, 250)
        thalach = st.slider('Max Heart Rate Achieved', 71, 202, 150)
        oldpeak = st.slider('ST Depression Induced by Exercise', 0.0, 6.2, 1.0, step=0.1)

        # Collect categorical inputs using the encoder's 'classes_' to get possible values
        sex = st.selectbox('Sex', encoder['Sex'].classes_)
        cp = st.selectbox('Chest Pain Type', encoder['ChestPainType'].classes_)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', ['Yes', 'No'])
        restecg = st.selectbox('Resting ECG', encoder['RestingECG'].classes_)
        exang = st.selectbox('Exercise Induced Angina', encoder['ExerciseAngina'].classes_)
        slope = st.selectbox('Slope of Peak Exercise ST Segment', encoder['ST_Slope'].classes_)

        # Map user input to the required format
        input_data = {
            'Age': age,
            'Sex': encoder['Sex'].transform([sex])[0],
            'ChestPainType': encoder['ChestPainType'].transform([cp])[0],
            'RestingBP': trestbps,
            'Cholesterol': chol,
            'FastingBS': 1 if fbs == 'Yes' else 0,  # Binary mapping
            'RestingECG': encoder['RestingECG'].transform([restecg])[0],
            'MaxHR': thalach,
            'ExerciseAngina': encoder['ExerciseAngina'].transform([exang])[0],
            'Oldpeak': oldpeak,
            'ST_Slope': encoder['ST_Slope'].transform([slope])[0]
        }
        return input_data
    except Exception as e:
        st.error(f"Error in collecting input features: {e}")
        return None

# Collect user input
user_input = user_input_features()

# Check if user input was successful
if user_input is None:
    st.stop()

# Convert user input to a DataFrame for prediction
input_df = pd.DataFrame([user_input])

# Display user input for verification
st.write("User Input:")
st.write(input_df)

# Make prediction
if st.button('Predict'):
    try:
        prediction = model.predict(input_df)
        if prediction[0] == 1:
            st.error("The model predicts that you are at risk for heart disease.")
        else:
            st.success("The model predicts that you are not at risk for heart disease.")
    except Exception as e:
        st.error(f"Error making prediction: {e}")
