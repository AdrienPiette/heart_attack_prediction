import streamlit as st

# Set page config
st.set_page_config(page_title="Heart Disease Dashboard", page_icon="❤️", layout="wide")

# Add a title to the page
st.title("Heart Disease Prediction App 💓")

# Add a description with emojis
st.write("""
Welcome to the **Heart Disease Prediction** application! 🏥✨
This app uses advanced machine learning techniques to predict whether a person is at risk of heart disease based on various health metrics. 💡

You can enter your details in the form below, and our trained model will provide a prediction on whether you're at risk of heart disease. ❤️

### Key Features:
- Predict the likelihood of heart disease based on personal health data 🩺
- Input data such as age, cholesterol levels, heart rate, etc. 📊
- Get results in real-time! ⚡

We use data-driven insights to help you stay healthy and informed. Let’s get started! 💪
""")

# Add an image of a heart or health-related icon
st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.P6mfTvCtb52a4w9EvAYalAHaHa%26pid%3DApi&f=1&ipt=ade79c8dbe792b6bb5ea3496321a66bbd0d31809fba63f82f9b1cee652d4b3ef&ipo=images", caption="Heart Disease Prediction", width=400)

# Add a call to action
st.write("Fill in the form below to get your prediction! 🚀")


