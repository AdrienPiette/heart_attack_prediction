import streamlit as st

# Set page config
st.set_page_config(page_title="Heart Disease Dashboard", page_icon="❤️", layout="wide")

# Sidebar navigation menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Prediction"])

# Home Page
if page == "Home":
    st.title("Heart Disease Dashboard - Home")
    st.subheader("Welcome to the Heart Disease Dashboard")
    st.write("This is the home page where you can navigate to different pages.")

# Page 1 (For Visualizations)
elif page == "Dashboard":
    st.title("Heart Disease Analysis - Page 1")
    st.write("This is page 1 where you can explore heart disease data visualizations.")
    import page_1  # Content of page 1

# Prediction Page (Page 2)
elif page == "Prediction":
    st.title("Heart Disease Prediction")
    import page_2  # Import Page 2 for prediction
