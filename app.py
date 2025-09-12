import streamlit as st
import pickle
import numpy as np
import pandas as pd


with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

def getgrade(percentage, status):
  if status == 'Fail':
    return 'E'
  if(percentage >= 90):
    return 'O'
  if(percentage >= 80):
    return 'A'
  if(percentage >= 70):
    return 'B'
  if(percentage >= 60):
    return 'C'
  if(percentage >= 40):
    return 'D'
  else :
    return 'E'

st.title("Student Performance Prediction")
st.write("Enter the student's details to predict their overall grade.")

gender = st.selectbox("Gender", ['female', 'male'])
race_ethnicity = st.selectbox("Race/Ethnicity", ['group A', 'group B', 'group C', 'group D', 'group E'])
parental_level_of_education = st.selectbox("Parental Level of Education", ["bachelor's degree", "some college", "master's degree", "associate's degree", "high school", "some high school"])
lunch = st.selectbox("Lunch", ['standard', 'free/reduced'])
test_preparation_course = st.selectbox("Test Preparation Course", ['none', 'completed'])
math_score = st.slider("Math Score", 0, 100)
reading_score = st.slider("Reading Score", 0, 100)
writing_score = st.slider("Writing Score", 0, 100)
gender_map = {'female': 0, 'male': 1}
race_ethnicity_map = {'group A': 1, 'group B': 2, 'group C': 3, 'group D': 4, 'group E': 5}
parental_education_map = {"bachelor's degree": 1, "some college": 4, "master's degree": 3, "associate's degree": 0, "high school": 2, "some high school": 5}
lunch_map = {'standard': 1, 'free/reduced': 0}
test_prep_map = {'none': 1, 'completed': 0}
passmarks = 40
pass_math = 1 if math_score >= passmarks else 0
pass_reading = 1 if reading_score >= passmarks else 0
pass_writing = 1 if writing_score >= passmarks else 0
total_score = math_score + reading_score + writing_score
percentage = np.ceil(total_score / 3)
status = 1 if pass_math == 1 and pass_reading == 1 and pass_writing == 1 else 0 

if st.button("Predict Grade"):
    input_data = pd.DataFrame([[ 
        gender_map[gender],
        race_ethnicity_map[race_ethnicity],
        parental_education_map[parental_level_of_education],
        lunch_map[lunch],
        test_prep_map[test_preparation_course],
        math_score,
        reading_score,
        writing_score,
        pass_math,
        pass_reading,
                pass_writing,
        total_score,
        percentage,
        status
    ]], columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score', 'writing score', 'pass_math', 'pass_reading', 'pass_writing', 'total_score', 'percentage', 'status'])
    scaled_input_data = scaler.transform(input_data)
    predicted_grade_encoded = model.predict(scaled_input_data)[0]

    st.write(f"Predicted Grade: {predicted_grade_encoded}")