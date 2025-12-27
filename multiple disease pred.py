# -*- coding: utf-8 -*-
"""
Created on Tue May 14 00:16:52 2024

@author: User
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html

# loading the saved models
diabetes_model = pickle.load(open("C:/Users/Rehan/Downloads/IDS PROJECT(077,057)/IDS PROJECT(077,057)/saved models/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("C:/Users/Rehan/Downloads/IDS PROJECT(077,057)/IDS PROJECT(077,057)/saved models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("C:/Users/Rehan/Downloads/IDS PROJECT(077,057)/IDS PROJECT(077,057)/saved models/parkinsons_model.sav" , 'rb'))

# Custom CSS to extend the navbar to full width and stretch the image
custom_css = """
<style>
    .css-18e3th9 {
        padding-top: 0 !important;
        width: 200%; /* Stretching the navbar */
    }
    .css-1d391kg {
        padding-top: 0 !important;
        width: 200%; /* Stretching the navbar */
    }
    .css-1d391kg .css-1v3fvcr {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 200%; /* Stretching the navbar */
    }
    .css-1d391kg .css-1v3fvcr > div {
        width: 200%;
        max-width: 200%;
    }
    .css-1d391kg .css-1v3fvcr > div > div {
        width: 200%;
        max-width: 200%;
        background-color: #f8f9fa;
        border-bottom: 1px solid #ddd;
        padding: 10px;
        text-align: center;
    }
    .stApp {
        width: 200%; /* Making the whole app content full-width */
    }
    .stImage {
        object-fit: cover; /* Making the image cover the entire page */
        width: 60vw; /* Setting width to full viewport width */
        height: 60vh; /* Setting height to full viewport height */
        border-radius: 20%;
    }
</style>
"""

# Inject custom CSS into the app
html(custom_css)

# Top-level navigation bar
selected_category = option_menu(
    menu_title=None,
    options=['Home', 'Disease Test', 'Contact Us'],
    icons=['house', 'clipboard-data', 'envelope'],
    default_index=0,
    orientation='horizontal'
)

if selected_category == 'Home':
  
    st.title("Welcome to the Multiple Disease Prediction System")
    st.write("Use this application to predict the likelihood of having Diabetes, Heart Disease, or Parkinson's Disease using Machine Learning models.")
    
    # Adding a logo at the top
   
    
    st.image("C:/Users/Rehan/Downloads/IDS PROJECT(077,057)/IDS PROJECT(077,057)/wallpaper.jpg", use_column_width=True)  # Adjusted to use full width
    
    # Rest of your code remains the same



elif selected_category == 'Disease Test':
    # Top-level navigation bar for disease tests
    with st.sidebar:
        selected_test = option_menu(
            "Disease Tests",
            ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
            icons=['activity', 'heart', 'person'],
            default_index=0
        )

    # Diabetes Prediction Page
    if selected_test == 'Diabetes Prediction':
        # page title
        st.title('Diabetes Prediction Using ML')

        # getting the input data from user
        # columns for input field
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

        # code for prediction
        diab_diagnosis = ''

        # creating button for prediction
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The Person is Diabetic'
            else:
                diab_diagnosis = 'The Person is Not Diabetic'

        st.success(diab_diagnosis)

    # Heart Disease Prediction Page
    elif selected_test == 'Heart Disease Prediction':
        # page title
        st.title('Heart Disease Prediction Using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        # code for Prediction
        heart_diagnosis = ''

        # creating a button for Prediction
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

        st.success(heart_diagnosis)


    # Parkinsons Prediction Page
    elif selected_test == 'Parkinsons Prediction':
        # page title
        st.title('Parkinsons Prediction Using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
            fo = st.text_input('Mean fundamental frequency (in Hz).')

        with col2:
            fhi = st.text_input('Max fundamental frequency (in Hz)')

        with col3:
            flo = st.text_input('Min fundamental frequency (in Hz)')

        with col1:
            Jitter_percent = st.text_input('MDVP : Jitter(%)')

        with col2:
            Jitter_Abs = st.text_input('MDVP : Jitter(Abs)')

        with col3:
            RAP = st.text_input('MDVP : RAP')

        with col1:
            PPQ = st.text_input('MDVP : PPQ')

        with col2:
            DDP = st.text_input('Jitter : DDP')

        with col3:
            Shimmer = st.text_input('MDVP : Shimmer')

        with col1:
            Shimmer_dB = st.text_input('MDVP : Shimmer(dB)')

        with col2:
            APQ3 = st.text_input('Shimmer : APQ3')

        with col3:
            APQ5 = st.text_input('Shimmer: APQ5')

        with col1:
            APQ = st.text_input('MDVP : APQ')

        with col2:
            DDA = st.text_input('DDA')

        # code for Prediction
        parkinsons_diagnosis = ''

        # creating a button for Prediction    
        if st.button("Parkinson's Test Result"):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA]])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)
elif selected_category == 'Contact Us':
    st.title("Contact Us")
    st.write("For any inquiries or support, please reach out to us at:")
    st.write("Email: support@xyzhealthcare.com")
    st.write("Phone: +1 123 456 7890")
    st.write("Address: 123 Main Street, New York, USA")
    st.map()
    
    # Display company details in the sidebar
    with st.sidebar:
       st.sidebar.title("Company Details")
       
       st.sidebar.markdown(
           """
           <div style=' padding:10px; border-radius:5px'>
               <div style='margin-bottom: 10px; '>
                <span style='font-size: 14px; color:  LIGHTBLUE;'>&#127970;<b>Company Name:</b></span><br>
                <span style='font-size: 14px;'>Bahria IT HealtCare</span>
                </div>
                <div style='margin-bottom: 10px;'>
                <span style='font-size: 14px; color:  LIGHTBLUE;'>&#127937; <b>Location:</b></span><br>
                <span style='font-size: 14px;'>Islamabad, PAK</span>
                </div>
                <div style='margin-bottom: 10px;'>
                <span style='font-size: 14px; color: LIGHTBLUE;'>&#128231; <b>Email:</b></span><br>
                <span style='font-size: 14px;'>info@xyzhealthcare.com</span>
                </div>
                <div style='margin-bottom: 10px;'>
                <span style='font-size: 14px; color: White;'>&#9742; <b style='color: LIGHTBLUE;'>Phone:</b></span><br>
                <span style='font-size: 14px;'>+92 123 456 7890</span>
                </div>
                <div style='margin-bottom: 10px;'>
                <span style='font-size: 14px; color: LIGHTBLUE;'>&#127758; <b>Website:</b></span><br>
                <span style='font-size: 14px;'><a href="www.linked-in.com/in/muhammad-rehan-khalid">www.linked-in.com/in/muhammad-rehan-khalid</a></span>
                </div>
            </div>
                """
                , unsafe_allow_html=True)

       st.sidebar.markdown("---")
            
       if st.sidebar.button("Contact Us", key="contact_btn"):
                # Add code to handle contact button click
            pass

            