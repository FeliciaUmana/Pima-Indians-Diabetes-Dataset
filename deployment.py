import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
from PIL import Image
print('Libraries loaded successfully')

#script_dir = os.path.dirname(os.path.abspath(_file_))
image_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(image_dir, "Diabetics-image.png")

#load model and scaler
loaded_model = joblib.load('diabetes_model.pkl')
loaded_scaler = joblib.load('scaler.pkl')
image = Image.open(image_path)
print('Model and scaler loaded successfully')

#creating streamlit app
st.title('DIABETICS PREDICTION APP')
st.image(image, width='stretch')
st.write('This app predict, if a patient is likely to have  Diabetics or Not. Enter their details below')
print('title and header created successfully')

#define input parameters
#Diabetics = st.selectbox('Are you diaabetic or not', option('Yes', 'No'))
Pregnancies = st.number_input('PREGNANCY - how many times a patient has been pregnant.', min_value = 1.000, max_value = 13.500, value =3.00000, step=0.01)
Glucose = st.number_input('GLUCOSE - what is the level of glucose to be a dibetic patient.',  min_value = 44.000, max_value = 199.00, value =117.00000, step=0.01)
BloodPressure = st.number_input('BLOODPRESSURE -  Normal blood pressure → below 80 mm Hg, High blood pressure → 80 mm Hg and above.',  min_value =40.000, max_value = 104.000, value =72.00000, step=0.01)
SkinThickness = st.number_input('SKINTHICKNESS - This measures the thickness of the triceps skin fold in millimetres.', min_value = 14.500, max_value = 42.500, value =29.15342, step=0.01)
Insulin = st.number_input('INSULIN - Records the level of insulin in the blood, Normal insulin → 16 to 166 mu U/ml, Above 166 → abnormally high.', min_value = 1.000, max_value = 13.500, value =3.00000, step=0.01)
BMI    = st.number_input ('BMI - Body Mass Index. It is calculated from a person"s weight and height.', min_value = 18.200, max_value = 50.250, value =32.40000, step=0.01)
DiabetesPedigree = st.number_input('DIABETES PEDIGREE - it measures how likely a person is to get diabetes based on their family history, Higher score.', min_value = 0.078, max_value = 1.200, value =0.37250, step=0.01 )
Age  = st.number_input('AGE - This is the age of the patient in years.', min_value = 21.000, max_value = 66.500, value =29.00000, step=0.01)


#prepare input data
cols = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigree','Age']

input_data = pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigree, Age]], columns=cols)
print('input data created successfully')  

#print scaled data
scaled_data = pd.DataFrame(loaded_scaler.transform(input_data), columns=cols)
print('scaled_data created successfully') 

#make prediction
if st.button('predict Diabetics'):
    prediction = loaded_model.predict(scaled_data)
    probability = loaded_model.predict_proba(scaled_data)
    result = 'You Are Likely To Have Diabetics, please the Doctor' if prediction[0] ==1 else 'You Are Not Likely To Have Diabetics'
    st.success(f'Prediction: {result}')
print('Prediction Done successfully')

print('Deployment Done successfully') 
