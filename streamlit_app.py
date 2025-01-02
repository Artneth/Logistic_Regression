import streamlit as st
import joblib

st.title("Describe person")
model = joblib.load('titanic_model.pkl')
 
Pclass  = st.text_input("Enter Passenger Class(1 to 3): ")
Age = st.text_input("Enter Age: ")
SibSp = st.text_input("Enter number of siblings / spouses aboard the Titanic: ")
Parch = st.text_input("Enter number of parents / children aboard the Titanic: ")
Fare = st.text_input("Enter ticket Fare: ")
sex = st.selectbox('Select Gender',('Female', 'Male'))
if sex == 'Female':
    Sex_female = True
    Sex_male = False
else :
    Sex_female = False
    Sex_male =True
st.write(Sex_female)