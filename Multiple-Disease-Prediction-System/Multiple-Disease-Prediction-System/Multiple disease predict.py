# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:12:12 2023

@author: Admin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu




#Loading the saved models

diabetes_model = pickle.load(open('C:/Users/akash/Downloads/my big data project/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/akash/Downloads/my big data project/saved_models/heart_disease_model.sav','rb'))


#Sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Home Page','Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons = ['person-circle','activity','heart'],
                           default_index = 0)
 
#Diabetes Prediction Page
if(selected == 'Home Page'):    

    # Title of the app
    
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url('https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm0zNzNiYXRjaDE1LWJnLTExLmpwZw.jpg');
            background-size: cover;
            opacity: 0.8; /* Adjust opacity value as needed */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Subheader
    st.markdown('# **Disease Prediction Web App**')

    st.markdown('This web app predicts various diseases using machine learning models. Please select the disease you would like to predict from the sidebar.')

    # Markdown
    st.markdown('### Features')
    st.markdown('* **Machine Learning Models**: Utilizes SVM, Logistic Regression.')
    st.markdown('* **Multiple Diseases**: Can predict diabetes, heart disease.')
    st.markdown('* **User-Friendly Interface**: Easy to navigate and use.')

    # Text
    st.markdown('''# Multiple Disease Prediction using Machine Learning and Streamlit''')
    st.markdown('''The Multiple Disease Prediction application is a machine learning-based project that aims to predict various diseases, including diabetes, heart disease. The application utilizes advanced machine learning algorithms such as Support Vector Machine (SVM),Logistic Regression.''')
    
    st.markdown('''This application offers a user-friendly interface with Two disease prediction options: heart disease and diabetes. Upon selecting a specific disease, the user is prompted to input the required parameters for the prediction model. Once the parameters are entered, the application utilizes  the trained models to predict the disease outcome and presents the result to the user.''')
    
    st.markdown('''The accuracy of the prediction models varies for each disease,with SVM achieving 78% accuracy for diabetes and logistic regression achieving 85% accuracy for heart disease.''')

    
    
    
    
    
    
#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    
    #Page title
    st.title('**Diabetes Prediction using ML**')

    st.markdown(
        f"""
        <style>
        body {{
            background-image: url('https://us.123rf.com/450wm/serezniy/serezniy1810/serezniy181047509/112408625-composition-with-glucometer-and-word-diabetes-made-of-wooden-cubes-on-color-background.jpg?ver=6');
            background-size: cover;
            opacity: 0.875; /* Adjust opacity value as needed */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('* **Number of Pregnancies**')
        
    with col2:
        Glucose = st.text_input('* **Glucose Level**')
    
    with col3:
        BloodPressure = st.text_input('* **Blood Pressure value**')
    
    with col1:
        SkinThickness = st.text_input('* **Skin Thickness value**')
    
    with col2:
        Insulin = st.text_input('* **Insulin Level**')
    
    with col3:
        BMI = st.text_input('* **BMI value**')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('* **Diabetes Pedigree Function value**')
    
    with col2:
        Age = st.text_input('* **Age of the Person**')
    
    
    #Code for prediction
    diab_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = '##### The person is Diabetic'
            
        else:
            diab_diagnosis = '##### The person is Not Diabetic'
            
            
    st.success(diab_diagnosis)

 
           
#Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    #Page title
    st.title('**Heart Disease Prediction using ML**')
    
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url('https://file.the-yuan.com/KUpload/image/20230116/20230116084737_9201.png');
            background-size: cover;
            opacity: 0.875; /* Adjust opacity value as needed */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')

    with col2:
        sex = st.number_input('Sex')

    with col3:
        cp = st.number_input('Chest Pain types')

    with col1:
        trestbps = st.number_input('Resting Blood Pressure')

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.number_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.number_input('* **ST depression induced by exercise**')

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.number_input('thal: 1 = normal; 2 = fixed defect; 3 = reversible defect')        
    
    
        
     
    #Code for prediction
    heart_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = '##### The person is suffering from Heart disease'
            
        else:
            heart_diagnosis = '##### The person is Not suffering from Heart disease'
            
    st.success(heart_diagnosis)





def set_bg_from_url(): 

    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                Made by Mohamed Kaif
                &nbsp;
                <a href="https://www.linkedin.com/in/themohamedkaif">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-linkedin" viewBox="0 0 16 16">
                        <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                    </svg>          
                </a>
                &nbsp;
                <a href="https://github.com/themohamedkaif">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-github" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                </a>
            </p>
        </div>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)

        
# Set background image from URL
set_bg_from_url()

 