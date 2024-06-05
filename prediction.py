import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load trained model and encoder
trained_model = joblib.load('model/trained_model.pkl')
encoder = joblib.load('model/encoder.pkl')

# Load the logo image
logo_path = "image/logo.png"

# Display the logo with a specific width
st.image(logo_path, width=200)

# Function to map education level to numeric values
def map_education(education):
    education_mapping = {
        'Below College': 1,
        'College': 2,
        'Bachelor Degree': 3,
        'Master': 4,
        'Doctor': 5
    }
    return education_mapping[education]

# Function to take user input
def user_input_features():
    Age = st.number_input('Age', min_value=18, max_value=70, value=30)
    BusinessTravel = st.selectbox('BusinessTravel', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    Department = st.selectbox('Department', ['Sales', 'Research & Development', 'Human Resources'])
    DistanceFromHome = st.number_input('DistanceFromHome', min_value=1, max_value=29, value=10)
    Education = st.selectbox('Education', ['Below College', 'College', 'Bachelor Degree', 'Master', 'Doctor'])
    EducationField = st.selectbox('EducationField', ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other'])
    EnvironmentSatisfaction = st.number_input('EnvironmentSatisfaction', min_value=1, max_value=4, value=3)
    JobInvolvement = st.number_input('JobInvolvement', min_value=1, max_value=4, value=3)
    JobRole = st.selectbox('JobRole', ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
    JobSatisfaction = st.number_input('JobSatisfaction', min_value=1, max_value=4, value=3)
    MaritalStatus = st.selectbox('MaritalStatus', ['Single', 'Married', 'Divorced'])
    MonthlyIncome = st.number_input('MonthlyIncome', min_value=1000, max_value=20000, value=5000)
    NumCompaniesWorked = st.number_input('NumCompaniesWorked', min_value=0, max_value=10, value=1)
    OverTime = st.selectbox('OverTime', ['Yes', 'No'])
    PercentSalaryHike = st.number_input('PercentSalaryHike', min_value=0, max_value=100, value=10)
    RelationshipSatisfaction = st.number_input('RelationshipSatisfaction', min_value=1, max_value=4, value=3)
    StockOptionLevel = st.number_input('StockOptionLevel', min_value=0, max_value=3, value=1)
    TrainingTimesLastYear = st.number_input('TrainingTimesLastYear', min_value=0, max_value=6, value=3)
    WorkLifeBalance = st.number_input('WorkLifeBalance', min_value=1, max_value=4, value=3)
    YearsInCurrentRole = st.number_input('YearsInCurrentRole', min_value=0, max_value=40, value=5)

    # Map selected education to numeric value
    education_numeric = map_education(Education)

    data = {
        'Age': Age,
        'BusinessTravel': BusinessTravel,
        'Department': Department,
        'DistanceFromHome': DistanceFromHome,
        'Education': education_numeric,
        'EducationField': EducationField,
        'EnvironmentSatisfaction': EnvironmentSatisfaction,
        'JobInvolvement': JobInvolvement,
        'JobRole': JobRole,
        'JobSatisfaction': JobSatisfaction,
        'MaritalStatus': MaritalStatus,
        'MonthlyIncome': MonthlyIncome,
        'NumCompaniesWorked': NumCompaniesWorked,
        'OverTime': OverTime,
        'PercentSalaryHike': PercentSalaryHike,
        'RelationshipSatisfaction': RelationshipSatisfaction,
        'StockOptionLevel': StockOptionLevel,
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'WorkLifeBalance': WorkLifeBalance,
        'YearsInCurrentRole': YearsInCurrentRole
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Main function to run the Streamlit app
def main():
    st.title('Attrition Prediction App')
    st.write("Enter the details below to predict the attrition:")

    # Get user input
    input_df = user_input_features()

    # Display the input
    st.subheader('User Input')
    st.write(input_df)

    # Encode selected columns using the one-hot encoder
    categorical_columns = ['BusinessTravel', 'Department', 'EducationField', 'JobRole', 'OverTime', 'MaritalStatus']
    encoded_cols = encoder.transform(input_df[categorical_columns])
    encoded_columns = encoder.get_feature_names_out(categorical_columns)
    input_df_encoded = pd.concat([input_df.drop(['BusinessTravel', 'Department', 'EducationField', 'JobRole', 'OverTime', 'MaritalStatus'], axis=1), pd.DataFrame(encoded_cols, columns=encoded_columns)], axis=1)

    # Predict Attrition
    if st.button('Predict'):
        prediction = trained_model.predict(input_df_encoded)
        prediction_proba = trained_model.predict_proba(input_df_encoded)

        st.subheader('Prediction')
        attrition_result = 'Yes' if prediction[0] == 1 else 'No'
        st.write(f'Attrition: {attrition_result}')

        st.subheader('Prediction Probability')
        st.write(f'Probability of Attrition: {prediction_proba[0][1]:.2f}')
        st.write(f'Probability of No Attrition: {prediction_proba[0][0]:.2f}')

if __name__ == '__main__':
    main()
