import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
diabetes_model = pickle.load(open('diabetes_saved_', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_saved', 'rb'))
liver_disease_model = pickle.load(open('liver_saved_model.pkl', 'rb'))  # Make sure this exists

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Liver Disease Prediction'],
                          icons=['activity','heart', 'droplet-half'],
                          default_index=0)

# ================= Diabetes Prediction Page ====================
if selected == 'Diabetes Prediction':
    st.title('🩸 Diabetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            input_data = [[float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]]
            diab_prediction = diabetes_model.predict(input_data)
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(diab_diagnosis)
        except:
            st.error("Please enter valid numerical values for all fields.")

# ================= Heart Disease Prediction Page ====================
if selected == 'Heart Disease Prediction':
    st.title('❤️ Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = male, 0 = female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0–3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0,1,2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes, 0 = no)')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Number of major vessels (0–3)')
    with col1:
        thal = st.text_input('Thal (1 = normal; 2 = fixed defect; 3 = reversible defect)')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                           float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                           float(ca), float(thal)]]
            heart_prediction = heart_disease_model.predict(input_data)
            heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
            st.success(heart_diagnosis)
        except:
            st.error("Please enter valid numerical values for all fields.")

# ================= Liver Disease Prediction Page ====================
if selected == 'Liver Disease Prediction':
    st.title('🧫 Liver Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age')
    with col2:
        Gender = st.selectbox('Gender', ['Male', 'Female'])
    with col3:
        Total_Bilirubin = st.text_input('Total Bilirubin')
    with col1:
        Direct_Bilirubin = st.text_input('Direct Bilirubin')
    with col2:
        Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase')
    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase')
    with col1:
        Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase')
    with col2:
        Total_Proteins = st.text_input('Total Proteins')
    with col3:
        Albumin = st.text_input('Albumin')
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio')

    liver_diagnosis = ''
    if st.button('Liver Disease Test Result'):
        try:
            gender_binary = 1 if Gender == 'Male' else 0
            input_data = [[float(Age), gender_binary, float(Total_Bilirubin), float(Direct_Bilirubin),
                           float(Alkaline_Phosphotase), float(Alamine_Aminotransferase),
                           float(Aspartate_Aminotransferase), float(Total_Proteins),
                           float(Albumin), float(Albumin_and_Globulin_Ratio)]]
            liver_prediction = liver_disease_model.predict(input_data)
            liver_diagnosis = 'The person has liver disease' if liver_prediction[0] == 1 else 'The person does not have liver disease'
            st.success(liver_diagnosis)
        except:
            st.error("Please enter valid numerical values for all fields.")
