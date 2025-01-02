import streamlit as st
import joblib
import pandas as pd

st.title("Give details to check if you would survive the Titanic Disaster (Accuracy: 80%)")
model = joblib.load('titanic_model.pkl')
 
Pclass_input = st.text_input("Enter Passenger Class(1 to 3): ")
Pclass = int(Pclass_input) if Pclass_input else 0

Age_input = st.text_input("Enter Age: ")
Age = int(Age_input) if Age_input else 0

SibSp_input = st.text_input("Enter number of siblings / spouses aboard the Titanic: ")
SibSp = int(SibSp_input) if SibSp_input else 0

Parch_input = st.text_input("Enter number of parents / children aboard the Titanic: ")
Parch = int(Parch_input) if Parch_input else 0

Fare_input = st.text_input("Enter ticket Fare: ")
Fare = int(Fare_input) if Fare_input else 0
sex = st.selectbox('Select Gender',('Female', 'Male'))
if sex == 'Female':
    Sex_female = True
    Sex_male = False
else :
    Sex_female = False
    Sex_male =True
embark = st.selectbox('Select port of Embarkation',('Cherbourg', 'Queenstown', 'Southampton'))
if embark == 'Cherbourg':
    Embarked_C = True
    Embarked_Q = False
    Embarked_S = False
elif embark == 'Queenstown':
    Embarked_C = False
    Embarked_Q = True
    Embarked_S = False
else:
    Embarked_C = False
    Embarked_Q = False
    Embarked_S = True
values = pd.DataFrame({'Pclass':[Pclass], 'Age':[Age], 'SibSp':[SibSp], 'Parch':[Parch], 'Fare':[Fare], 'Sex_female':[Sex_female], 
                       'Sex_male':[Sex_male],	'Embarked_C':[Embarked_C], 'Embarked_Q':[Embarked_Q], 'Embarked_S':[Embarked_S]})
y = model.predict(values)
if y == 0:
    st.subheader("0, Would Not Survive")
else:
    st.subheader("1, Would Survive")

st.title("To Check for multiple entries,")
st.write("Provide csv file with columns:" 
         " [Pclass, Age, SibSp, Parch, Fare, Sex_female, Sex_male, Embarked_C, Embarked_Q, Embarked_S]")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    data.columns = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S']
    Y = model.predict(data)
    st.write(Y)

                    