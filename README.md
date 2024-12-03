❤️ Heart Disease Prediction with Machine Learning
🩺 Context

Cardiovascular diseases (CVDs) are the leading cause of death worldwide, claiming approximately 17.9 million lives each year, which is 31% of all deaths globally. Heart attacks and strokes account for most of these deaths, many of which occur prematurely in people under 70 years of age.

This project focuses on early detection of heart disease using machine learning models. Early intervention for individuals at risk due to factors like hypertension, diabetes, or high cholesterol can save lives. 🚑
📊 Dataset
🔎 Overview

The dataset combines information from five major heart disease datasets, resulting in 918 unique observations across 11 features. This comprehensive dataset enables accurate heart disease predictions.
🏷️ Attribute Information

    Age: Patient's age (in years).
    Sex: Patient's sex (M: Male, F: Female).
    ChestPainType: Type of chest pain:
        TA: Typical Angina.
        ATA: Atypical Angina.
        NAP: Non-Anginal Pain.
        ASY: Asymptomatic.
    RestingBP: Resting blood pressure (mm Hg).
    Cholesterol: Serum cholesterol level (mg/dl).
    FastingBS: Fasting blood sugar (1: >120 mg/dl, 0: ≤120 mg/dl).
    RestingECG: Resting electrocardiogram results:
        Normal: Normal ECG.
        ST: ST-T wave abnormalities.
        LVH: Left ventricular hypertrophy.
    MaxHR: Maximum heart rate achieved.
    ExerciseAngina: Exercise-induced angina (Y: Yes, N: No).
    Oldpeak: ST segment depression during exercise.
    ST_Slope: Slope of the ST segment:
        Up: Upsloping.
        Flat: Flat.
        Down: Downsloping.
    HeartDisease: Target variable (1: Heart disease, 0: Normal).

🌐 Source

The dataset is curated by combining:

    Cleveland: 303 observations.
    Hungarian: 294 observations.
    Switzerland: 123 observations.
    Long Beach VA: 200 observations.
    Stalog: 270 observations.

🔗 For more details, visit the UCI Machine Learning Repository.
🎯 Project Goals

    📈 Exploratory Data Analysis (EDA):
        Visualize distributions of age, sex, cholesterol, etc.
        Analyze correlations between features and heart disease.

    🔧 Feature Engineering:
        Clean and preprocess data.
        Engineer features to improve model accuracy.

    🤖 Predictive Modeling:
        Train machine learning models to predict heart disease.
        Evaluate models using accuracy, precision, recall, and AUC-ROC.

    🌐 Deployment:
        Build an interactive dashboard for real-time predictions.

🛠️ Tools and Libraries

    🐍 Python for data analysis and modeling.
    📊 Pandas and NumPy for data manipulation.
    🎨 Matplotlib, Seaborn, and Plotly for visualizations.
    🧠 Scikit-learn for machine learning.
    ⚙️ Streamlit or Flask for deployment (optional).

🚀 Installation

    Clone the repository:

git clone https://github.com/your-repo/heart-disease-prediction.git
cd heart-disease-prediction

Install dependencies:

    pip install -r requirements.txt

🏃 Usage
📊 Data Visualization

Explore patterns and trends in the data:

python visualize_data.py

🤖 Model Training

Train the machine learning model:

python train_model.py

🌐 Deployment (Optional)

Launch the interactive web app:

streamlit run app.py

🤝 Contributing

Feel free to open issues or submit pull requests if you'd like to contribute. Contributions are welcome! 🎉
📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.