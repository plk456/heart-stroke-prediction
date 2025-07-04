import streamlit as st
import pickle
import numpy as np
import os

try:
    with open('Models\\model', 'rb') as f:
        model=pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None    
    print('file None')

gender=st.selectbox("patient gender",['Male',"Female"])
if gender=='Male':
    gender=1
else:
    gender=0

age=st.text_input("patient your age")

st.title("Stroke Prediction App")

hypertension=st.selectbox("patient have hypertension?", ["Yes", "No"])
hypertension=1 if hypertension =="yes" or "Yes" else 0

heart_disease=st.selectbox("Do patient have heart disease?", ["Yes", "No"])
heart_disease=0 if heart_disease =="No" or "no" else 1

ever_married=st.selectbox("Are you ever married?", ["Yes", "No"])
ever_married=1 if ever_married=="yes"or "Yes" else 0

work_type=st.selectbox("What is your work type?", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
if work_type == "Private":
    work_type = 0
elif work_type == "Self-employed":
    work_type = 1
elif work_type == "Govt_job":
    work_type = 2
elif work_type == "children":
    work_type = 3
else:
    work_type = 4

residence_type=st.selectbox("What is your residence type?", ["Urban", "Rural"])
if residence_type == "Urban":
    residence_type = 0
else:
    residence_type = 1

avg_glucose_level=st.number_input("Enter patient average glucose level")

bmi=st.text_input("Enter your BMI")
if bmi == "":
    bmi = 0.0
smoking_status=st.selectbox("What is patients smoking status?", ["formerly smoked", "never smoked", "smokes", "Unknown"])
if smoking_status == "formerly smoked":
    smoking_status = 0
elif smoking_status == "never smoked":
    smoking_status = 1
elif smoking_status == "smokes":
    smoking_status = 2
else:
    smoking_status = 3

if st.button('Predict'):
    # Create input array
    input_data = np.array([[
        gender,
        age,
        hypertension,
        heart_disease,
        ever_married,
        work_type,
        residence_type,
        avg_glucose_level,
        bmi,
        smoking_status
    ]])
    
    prediction = model.predict(input_data)
    
    prediction_proba = model.predict_proba(input_data)
    
    stroke_probability = prediction_proba[0][1] * 100  # Probability of class 1 (High Risk)
    
    st.write(f'Probability of stroke: {stroke_probability:.2f}%')
    st.write(f'Prediction: {"High Risk" if prediction[0] == 1 else "Low Risk"}')