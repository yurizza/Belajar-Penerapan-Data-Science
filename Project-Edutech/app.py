import streamlit as st
import pandas as pd
from joblib import load
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Memuat model dan scaler
model = load('model/best_trained_model.pkl')
standard_scaler = load('model/best_standard_scaler.pkl')

# Judul aplikasi
st.title("Prediksi Status Mahasiswa")

# Menambahkan logo di sidebar
st.sidebar.image('image/logo.png', use_column_width=True)
# Sidebar untuk menu
menu = st.sidebar.selectbox('Menu', ['Prediction', 'Show Summary Image'])

if menu == 'Prediction':
    st.header('Masukkan Parameter Mahasiswa')

    def user_input_features():
        Application_order = st.slider('Application_order', 1, 10, 1)
        Daytime_evening_attendance = st.selectbox('Daytime_evening_attendance', ('Daytime', 'Evening'))
        Previous_qualification_grade = st.slider('Previous_qualification_grade', 0.0, 190.0, 90.0)
        Admission_grade = st.slider('Admission_grade', 0.0, 190.0, 90.0)
        Displaced = st.selectbox('Displaced', ('Yes', 'No'))
        Debtor = st.selectbox('Debtor', ('Yes', 'No'))
        Tuition_fees_up_to_date = st.selectbox('Tuition_fees_up_to_date', ('Yes', 'No'))
        Gender = st.selectbox('Gender', ('Male', 'Female'))
        Scholarship_holder = st.selectbox('Scholarship_holder', ('Yes', 'No'))
        Curricular_units_1st_sem_credited = st.slider('Curricular_units_1st_sem_credited', 0, 30, 0)
        Curricular_units_1st_sem_enrolled = st.slider('Curricular_units_1st_sem_enrolled', 0, 30, 0)
        Curricular_units_1st_sem_approved = st.slider('Curricular_units_1st_sem_approved', 0, 30, 0)
        Curricular_units_1st_sem_grade = st.slider('Curricular_units_1st_sem_grade', 0.0, 30.0, 0.0)
        Curricular_units_2nd_sem_credited = st.slider('Curricular_units_2nd_sem_credited', 0, 20, 0)
        Curricular_units_2nd_sem_enrolled = st.slider('Curricular_units_2nd_sem_enrolled', 0, 20, 0)
        Curricular_units_2nd_sem_approved = st.slider('Curricular_units_2nd_sem_approved', 0, 20, 0)
        Curricular_units_2nd_sem_grade = st.slider('Curricular_units_2nd_sem_grade', 0.0, 30.0, 0.0)
        
        data = {
            'Application_order': Application_order,
            'Daytime_evening_attendance': 1 if Daytime_evening_attendance == 'Daytime' else 0,
            'Previous_qualification_grade': Previous_qualification_grade,
            'Admission_grade': Admission_grade,
            'Displaced': 1 if Displaced == 'Yes' else 0,
            'Debtor': 1 if Debtor == 'Yes' else 0,
            'Tuition_fees_up_to_date': 1 if Tuition_fees_up_to_date == 'Yes' else 0,
            'Gender': 1 if Gender == 'Male' else 0,
            'Scholarship_holder': 1 if Scholarship_holder == 'Yes' else 0,
            'Curricular_units_1st_sem_credited': Curricular_units_1st_sem_credited,
            'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
            'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
            'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
            'Curricular_units_2nd_sem_credited': Curricular_units_2nd_sem_credited,
            'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
            'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
            'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
        }
        features = pd.DataFrame(data, index=[0])
        return features

    df_input = user_input_features()

    # Menampilkan input pengguna
    st.subheader('Parameter Mahasiswa')
    st.write(df_input)
    # Define categorical features
    numerical_features = ['Application_order','Previous_qualification_grade','Admission_grade',
                        'Curricular_units_1st_sem_enrolled','Curricular_units_2nd_sem_enrolled',
                        'Curricular_units_1st_sem_credited','Curricular_units_2nd_sem_credited',
                        'Curricular_units_1st_sem_approved','Curricular_units_2nd_sem_approved',
                        'Curricular_units_1st_sem_grade','Curricular_units_2nd_sem_grade']
    # Create preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('scaler', standard_scaler, numerical_features)
        ],
        remainder='passthrough'
    )

    # Add the preprocessor and model to the pipeline
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])

    # Fit preprocessor to df_enrolled (assuming this is necessary for standard scaler)
    pipeline.named_steps['preprocessor'].fit(df_input)

    # Preprocess and predict using df_enrolled
    y_pred_test = pipeline.predict(df_input)

    # Prediksi probabilitas
    if hasattr(model, 'predict_proba'):
        y_pred_proba = pipeline.predict_proba(df_input)
    else:
        y_pred_proba = None

    st.subheader('Hasil Prediksi')
    # Konversi prediksi menjadi label yang mudah dipahami
    status = 'Dropout' if y_pred_test[0] == 1 else 'Graduate'
    # Menentukan warna teks berdasarkan prediksi
    color = 'red' if status == 'Dropout' else 'green'
    # Menampilkan prediksi dan probabilitasnya dengan warna yang sesuai
    if y_pred_proba is not None:
        proba = round(y_pred_proba[0][y_pred_test[0]], 3)  # Ambil probabilitas dari kelas prediksi
        st.markdown(f'<p style="color:{color}">{status} dengan probabilitas {proba}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p style="color:{color}">{status} (Probabilitas tidak tersedia)</p>', unsafe_allow_html=True)
    

elif menu == 'Show Summary Image':
    st.header('Penjelasan Model dan Feature Importances')

    # Menampilkan informasi dengan Streamlit
    st.write("""
    Model yang digunakan untuk prediksi status mahasiswa adalah model yang sudah dilatih dengan berbagai fitur
    yang relevan. Model ini menggunakan teknik machine learning dengan Random Forest untuk memprediksi apakah seorang mahasiswa akan Graduate
    atau Dropout berdasarkan input fitur yang diberikan.

    Berikut parameter model:
    """)
    model_params = model.get_params()
    # Menampilkan parameter model dengan rapi dalam format JSON
    if isinstance(model_params, dict):
        st.json(model_params)
    else:
        st.write(model_params)

    # Menampilkan gambar feature importances
    st.image('image/feature_importances.png', caption='Feature Importances')
