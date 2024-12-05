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

# Sidebar navigation menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Prediction"])

# Home Page
if page == "Home":
    st.title("Heart Disease Dashboard - Home")
    st.subheader("Welcome to the Heart Disease Dashboard")
    st.write("This is the home page where you can navigate to different pages.")
    st.write("Select a page from the sidebar to explore more!")

# Page 1 (For Visualizations)
elif page == "Dashboard":
    st.title("Heart Disease Analysis - Dashboard")
    st.write("This is page 1 where you can explore heart disease data visualizations.")
    # Example of a visualization placeholder
    st.write("Visualizations will be shown here.")
    # Import page_1 only when the user selects the Dashboard page
    import page_1  # Ensure this script exists

# Prediction Page (Page 2)
elif page == "Prediction":
    st.title("Heart Disease Prediction")
    st.write("Enter your health details in the form below to predict your risk of heart disease.")
    # Import page_2 only when the user selects the Prediction page
    import page_2  # Ensure this script exists

