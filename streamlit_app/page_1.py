import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv(r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Data\heart_cleaned.csv')

# Display the first few rows of the data
st.title("Heart Disease Dashboard")
st.subheader("Data Preview")
st.write(data.head())

# Initialize the encoder
encoder = LabelEncoder()

# Encoding categorical columns
categorical_columns = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope', 'FastingBS']  # Add all categorical columns that need encoding

# Apply encoding for each categorical column
for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])

# Create and display the plots

# 1 - Age Distribution by Heart Disease
fig = px.histogram(
    data, 
    x='Age', 
    color='HeartDisease', 
    nbins=30, 
    color_discrete_sequence=['Orange', 'Teal'],
    title='Age Distribution with Heart Disease'
)
fig.update_layout(
    xaxis_title='Age',
    yaxis_title='Count',
    legend_title='Heart Disease',
    template='plotly_white',
    title_font_size=16,
    title_x=0.5
)
st.subheader("Age Distribution by Heart Disease")
st.plotly_chart(fig, use_container_width=True)

# 2 - Sex Distribution by Heart Disease
fig_2 = px.histogram(
    data, 
    x='Sex', 
    color='HeartDisease', 
    barmode='stack', 
    color_discrete_sequence=['Orange', 'Teal'], 
    title='Heart Disease Distribution by Sex'
)
fig_2.update_layout(
    xaxis_title='Sex',
    yaxis_title='Count',
    legend_title='Heart Disease',
    template='plotly_white',
    title_font_size=16,
    title_x=0.5,  
    yaxis=dict(range=[0, 800])  
)
st.subheader("Sex Distribution by Heart Disease")
st.plotly_chart(fig_2, use_container_width=True)

# 3 - Chest Pain Type Distribution by Heart Disease
fig_3 = px.histogram(
    data, 
    x='ChestPainType', 
    color='HeartDisease', 
    barmode='group', 
    color_discrete_sequence=['Orange', 'Teal'], 
    title='Heart Disease Distribution by Chest Pain Type'
)
fig_3.update_layout(
    xaxis_title='Chest Pain Type',
    yaxis_title='Count',
    legend_title='Heart Disease',
    template='plotly_white',
    title_font_size=16,
    title_x=0.5,
    yaxis=dict(range=[0, 300])  
)
st.subheader("Chest Pain Type Distribution by Heart Disease")
st.plotly_chart(fig_3, use_container_width=True)

# 4 - Heart Disease Distribution by ST Slope
fig_4 = px.histogram(
    data, 
    x='ST_Slope', 
    color='HeartDisease', 
    barmode='group', 
    color_discrete_sequence=['Orange', 'Teal'], 
    title='Heart Disease Distribution by ST Slope'
)
fig_4.update_layout(
    xaxis_title='ST Slope',
    yaxis_title='Count',
    legend_title='Heart Disease',
    template='plotly_white',
    title_font_size=16,
    title_x=0.5,  
    yaxis=dict(range=[0, 300])  
)
st.subheader("Heart Disease Distribution by ST Slope")
st.plotly_chart(fig_4, use_container_width=True)

# 5 - Heart Disease Distribution by Fasting Blood Sugar
fig_5 = px.histogram(
    data, 
    x='FastingBS', 
    color='HeartDisease', 
    barmode='group', 
    color_discrete_sequence=['Orange', 'Teal'], 
    title='Heart Disease Distribution by Fasting Blood Sugar'
)
fig_5.update_layout(
    xaxis_title='Fasting Blood Sugar',
    yaxis_title='Count',
    legend_title='Heart Disease',
    template='plotly_white',
    title_font_size=16,
    title_x=0.5,  
    yaxis=dict(range=[0, 300])  
)
st.subheader("Heart Disease Distribution by Fasting Blood Sugar")
st.plotly_chart(fig_5, use_container_width=True)

# 6 - Heart Disease Distribution by Resting ECG
fig_6 = px.histogram(
    data, 
    x='RestingECG', 
    color='HeartDisease', 
    barmode='group', 
    color_discrete_sequence=['Orange', 'Teal'], 
    title='Heart Disease Distribution by Resting ECG'
)
fig_6.update_layout(
    xaxis_title='Resting ECG',
    yaxis_title='Count',
    legend_title='Heart Disease',
    template='plotly_white',
    title_font_size=16,
    title_x=0.5,  
    yaxis=dict(range=[0, 300])  
)
st.subheader("Heart Disease Distribution by Resting ECG")
st.plotly_chart(fig_6, use_container_width=True)

# 7 - Heart Disease Distribution by Exercise Angina
fig_7 = px.histogram(
    data, 
    x='ExerciseAngina', 
    color='HeartDisease', 
    barmode='group', 
    color_discrete_sequence=['Orange', 'Teal'], 
    title='Heart Disease Distribution by Exercise Angina'
)
fig_7.update_layout(
    xaxis_title='Exercise Angina',
    yaxis_title='Count',
    legend_title='Heart Disease',
    template='plotly_white',
    title_font_size=16,
    title_x=0.5,  
    yaxis=dict(range=[0, 300])  
)
st.subheader("Heart Disease Distribution by Exercise Angina")
st.plotly_chart(fig_7, use_container_width=True)

# 8 - Cholesterol Distribution by Heart Disease
fig_8 = px.histogram(
    data, 
    x='Cholesterol', 
    color='HeartDisease', 
    nbins=30,  
    color_discrete_sequence=['Orange', 'Teal'], 
    title='Cholesterol Distribution by Heart Disease'
)
fig_8.update_layout(
    xaxis_title='Cholesterol',
    yaxis_title='Count',
    legend_title='Heart Disease',
    template='plotly_white',
    title_font_size=16,
    title_x=0.5  
)
st.subheader("Cholesterol Distribution by Heart Disease")
st.plotly_chart(fig_8, use_container_width=True)

# 9 - Correlation Matrix for Heart Disease
corr = round(data.corr(), 2)  # Directly using the encoded data
fig_9 = px.imshow(
    corr, 
    color_continuous_scale='Viridis',  
    text_auto=True,  
    title='Correlation Matrix for Heart Disease'
)
fig_9.update_layout(
    template='plotly_white',
    title_font_size=16,
    title_x=0.5  
)
st.subheader("Correlation Matrix for Heart Disease")
st.plotly_chart(fig_9, use_container_width=True)

# 10 - Most Correlated Features with Heart Disease
corr_heartdisease = corr['HeartDisease'].sort_values(ascending=False)
corr_heartdisease = corr_heartdisease[1:]  # Remove the target variable

fig_10 = px.bar(
    corr_heartdisease, 
    x=corr_heartdisease.index, 
    y=corr_heartdisease.values, 
    color=corr_heartdisease.values,  
    color_continuous_scale='Viridis',  
    title='Most Correlated Features with Heart Disease'
)
fig_10.update_layout(
    xaxis_title='Feature',
    yaxis_title='Correlation',
    coloraxis_colorbar=dict(title='Correlation'),
    template='plotly_white',
    title_font_size=16,
    title_x=0.5  
)
st.subheader("Most Correlated Features with Heart Disease")
st.plotly_chart(fig_10, use_container_width=True)
