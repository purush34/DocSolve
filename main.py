
import pickle
# from sqlite3 import Row
import streamlit as st
# from streamlit_option_menu import option_menu
#from model import Disease
# import os
# from PIL import Image
# import pandas as pd
# import pyautogui

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
# with st.sidebar:
    
#     selected = option_menu('Multiple Disease Prediction System',
                          
#                           ['Diabetes Prediction',
#                            'Heart Disease Prediction',
#                            'Parkinsons Prediction'],
#                           icons=['activity','heart','person'],
#                           default_index=0)

col1, col2 = st.columns([2,2], gap="small")

with col1:

    st.title("Doctor At Lap")
with col2:    
    st.image("logo.png", width=150)
st.write("Skip the travel, The right cure for you wherever you are, Consult our doctor bot to test yourself. ")
 
st.image("template.jpg", use_column_width='auto')

with st.expander("What can you find/get here?"):
    st.write("In this website you can get a better solution for problems such as Diabetis, Heart Diseases and Parkinson's Disease. Here we analyse your symptoms or metrics to find out whether you are infected with the disease or not. If found infected our expert doctor bot will give u precautions to be kept in mind and also medications to cure the disease but it is always adivisable to visit doctor after you get your test results because most of the medications that are suggested by our bot needs a doctor prescription to buy.")

    
tab1, tab2, tab3 = st.tabs(["Diabetis Prediction", "Heart Disease Prediction", " Parkinsons prediction"])
    
# Diabetes Prediction Page
# if (selected == 'Diabetes Prediction'):

with tab1:
    
    st.title('Diabetes Prediction using ML')
    
    with st.expander("What is Diabetis"):
        st.write("Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.")
        
    with st.expander("Prerequisite tests needed to be done:"):
        st.write("1. Glycated hemoglobin (A1C) test - To finding glucose content in our body")
        st.write("2. Skinfold measurement - To find Skin thickness")
        st.write("3. Fasting plasma glucose (FPG) test - To find Insulin content in our body")
        
    with st.expander("How does our doctor work:"):
        st.write("First you need to select your gender because diabetis metrics vary from male to female. After selecting your gender few more coloumns will appear, you need to fill in all coloumns from the tests done earlier. Our expert Bot will analyse your metrics and then identifies if you have diabetis or not. Along with the result our expert bot will give you precautions to be followed and medication that needed to be taken.")
    
    option = st.selectbox(
     'Please specify your gender?',
     ('Select','Male', 'Female'), key=2)
    
    if(option == 'Select'):
        st.write("Please select your Gender")
    
    if (option == 'Male'):
    
    
        # page title
        
        
        
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)
        
        # with col1:
        #     Pregnancies = st.text_input('Number of Pregnancies')
        
        Pregnancies = 0
        
            
        with col1:
            Glucose = st.slider('Glucose level', 0, 200, 100)
            st.write(Glucose)
        
        with col2:
            BloodPressure = st.slider('Blood Pressure level', 0, 130, 72)
            st.write(BloodPressure)
        
        with col3:
            SkinThickness = st.slider('Skin Thickness Value', 0, 100, 50)
            st.write(SkinThickness)
        
        with col1:
            Insulin = st.number_input('Insulin Level', min_value=0, value=0, step=1)
            st.write(Insulin)
        
        with col2:
            BMI = st.number_input('BMI Value', min_value=0.0, value=0.0, step=0.1)
            st.write(BMI)
        
        with col3:
            DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.00, value=0.00, step=0.01)
            st.write(DiabetesPedigreeFunction)
        
        with col1:
            Age = st.slider('Age', 0, 130, 65, key=4)
            st.write(Age)
            
        
        # code for Prediction
        diab_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
             diab_diagnosis = 'The person is diabetic'
             st.warning(diab_diagnosis)
             with st.expander("Medication"):
                 st.write("mediceesz")
             with st.expander("Precautions to avoid Diabetis"):
                 st.write("1. Quit Smoking")
                 st.write("2. Keep your BP and Cholestrol under control")
                 st.write("3. Keep up your Physical activity")
                 st.write("4. Maintain narmal BMI")
                 st.write("5. Take in healthy fats")
                 st.write("6. Drink more water")
            else:
             diab_diagnosis = 'The person is not diabetic'
             st.success(diab_diagnosis)
             with st.expander("Precautions to avoid Diabetis"):
                 st.write("1. Quit Smoking")
                 st.write("2. Keep your BP and Cholestrol under control")
                 st.write("3. Keep up your Physical activity")
                 st.write("4. Maintain narmal BMI")
                 st.write("5. Take in healthy fats")
                 st.write("6. Drink more water")
             
        # if st.button('Reset all parameters', key=15):
        #     pyautogui.hotkey("ctrl","F5")

        
    if (option== 'Female'):
         # page title
        
        
        
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Pregnancies = st.number_input('No. of Pregnancies', min_value=0, value=0, step=1)
            st.write(Pregnancies)
            
        with col2:
            Glucose = st.slider('Glucose level', 0, 200, 100)
            st.write(Glucose)
        
        with col3:
            BloodPressure = st.slider('Blood Pressure level', 0, 130, 72)
            st.write(BloodPressure)
        
        with col1:
            SkinThickness = st.slider('Skin Thickness Value', 0, 100, 50)
            st.write(SkinThickness)
        
        with col2:
            Insulin = st.number_input('Insulin Level', min_value=0, value=0, step=1)
            st.write(Insulin)
        
        with col3:
            BMI = st.number_input('BMI Value', min_value=0.0, value=0.0, step=0.1)
            st.write(BMI)
        
        with col1:
            DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.00, value=0.00, step=0.01)
            st.write(DiabetesPedigreeFunction)
        
        with col2:
            Age = st.slider('Age', 0, 130, 65, key=5)
            st.write(Age)
        
        
        # code for Prediction
        diab_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
                st.warning(diab_diagnosis)
                with st.expander("Medication"):
                 st.write("mediceesz")
                with st.expander("Precautions to avoid Diabetis"):
                 st.write("1. Quit Smoking")
                 st.write("2. Keep your BP and Cholestrol under control")
                 st.write("3. Keep up your Physical activity")
                 st.write("4. Maintain narmal BMI")
                 st.write("5. Take in healthy fats")
                 st.write("6. Drink more water")
            else:
                diab_diagnosis = 'The person is not diabetic'
                st.success(diab_diagnosis)
                with st.expander("Precautions to avoid Diabetis"):
                 st.write("1. Quit Smoking")
                 st.write("2. Keep your BP and Cholestrol under control")
                 st.write("3. Keep up your Physical activity")
                 st.write("4. Maintain narmal BMI")
                 st.write("5. Take in healthy fats")
                 st.write("6. Drink more water")
        
        # if st.button('Reset all parameters', key=14):
        #     pyautogui.hotkey("ctrl","F5")
        # st.success(diab_diagnosis)




# Heart Disease Prediction Page
# if (selected == 'Heart Disease Prediction'):

with tab2:
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    with st.expander("what are heart diseases:"):
        st.write("A type of disease that affects the heart or blood vessels. The risk of certain heart diseases may be increased by smoking, high blood pressure, high cholesterol, unhealthy diet, lack of exercise, and obesity.")
        
    with st.expander("Prerequisite tests needed to be done:"):
        st.write("1. Cholestrol Test - To find Serum Cholestrol")
        st.write("2. Glucose Tolerance Test - To find Fasting Blood Sugar")
        st.write("3. Electro cardiogram - To find electro cardiography")
        st.write("4. Flouroscopy - to check colored vessels in body")
        
    with st.expander("How does our bot work:"):
        st.write("First you need to fill in all coloumns from the tests done earlier. Our expert Bot will analyse your metrics and then identifies if you have heart disease or not. Along with the result our expert bot will give you precautions to be followed and medication that needed to be taken.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.slider('Age', 0, 130, 65, key=6)
        st.write(age)
        
    with col2:
        cp = st.slider('Rate if any chest pain on scale of 0 to 3', 0, 3, 0)
        st.write(cp)       

    with col3:
        trestbps = st.slider('Resting Blood Pressure', 0, 250, 125)
        st.write(trestbps)


        
    with col1:
        option3 = st.selectbox(
     'Please specify your FBS Value',
     ('Select','Fasting Blood Sugar < 120mg/dl', 'Fasting Blood Sugar > 120mg/dl'), key=7)
        if (option3 == 'Select'):
            st.write("Please select your option")
        if (option3 == 'Fasting Blood Sugar < 120mg/dl'):
            fbs = 0
            st.write(fbs)
        if (option3 == 'Fasting Blood Sugar > 120mg/dl'):
            fbs = 1
            st.write(fbs)
        
    with col2:
        option4 = st.selectbox(
     'Please specify your Restcg Results?',
     ('Select','positive', 'negative', 'normal'), key=8)
        if (option4 == 'Select'):
            st.write("Please select your Restcg")
        if (option4 == 'positive'):
            restecg = 0
            st.write(restecg)
        if (option4 == 'negative'):
            restecg = 1
            st.write(restecg)
        if (option4 == 'normal'):
            restecg = 2
            st.write(restecg)

        
    with col3:
        
        option2 = st.selectbox(
     'Please specify your gender?',
     ('Select','Male', 'Female'), key=3)
        if (option2 == 'Select'):
            st.write("Please select your gender")
        if (option2 == 'Male'):
            sex = 0
            st.write(sex)
        if (option2 == 'Female'):
            sex = 1
            st.write(sex)
        
    with col1:
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0, value=0, step=1)
        st.write(chol)
        
    with col2:
        thalach = st.number_input('Maximum Heart rate achieved', min_value=0, value=0, step=1)
        st.write(thalach)
        
    with col3:
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, value=0.0, step=0.1)
        st.write(oldpeak)

        
    with col1:
        option5 = st.selectbox(
     'Please specify your EIA?',
     ('Select','positive', 'negative'), key=9)
        if (option5 == 'Select'):
            st.write("Please select your exang")
        if (option5 == 'positive'):
            exang = 0
            st.write(exang)
        if (option5 == 'negative'):
            exang = 1
            st.write(exang)
        
    with col2:
        option6 = st.selectbox(
     'Please specify your thal?',
     ('Select','normal', 'fixed defect', 'reversable effect', 'normal'), key=10)
        if (option6 == 'Select'):
            st.write("Please select your thal")
        if (option6 == 'normal'):
            thal = 0
            st.write(thal)
        if (option6 == 'fixed defect'):
            thal = 1
            st.write(thal)
        if (option6 == 'reversable effect'):
            thal = 2
            st.write(thal)
        if (option6 == 'normal'):
            thal = 3
            st.write(thal)
        
    with col3:
        option7 = st.selectbox(
     'Please specify your ca?',
     ('Select','color1', 'color2', 'color3', 'color4', 'color5'), key=11)
        if (option7 == 'Select'):
            st.write("Please select your ca")
        if (option7 == 'color1'):
            ca = 0
            st.write(ca)
        if (option7 == 'color2'):
            ca = 1
            st.write(ca)
        if (option7 == 'color3'):
            ca = 2
            st.write(ca)
        if (option7 == 'color4'):
            ca = 3
            st.write(ca)
        if (option7 == 'color5'):
            ca = 4
            st.write(ca)
        
    with col1:
        slope = st.slider('Slope of the peak exercise ST segment specify slide', 0, 2, 0, key=12)
        st.write(slope)

 
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
          st.warning(heart_diagnosis)
          with st.expander("Symptoms "):
            st.write("rgrsf")
          with st.expander("Medications"):
              st.write("a")
        else:
          heart_diagnosis = 'The person does not have any heart disease'
          st.success(heart_diagnosis)
        
    
 
         
    #st.success(heart_diagnosis)
    
          
    
    # if st.button('Reset all Parameters', key=13):
    #     pyautogui.hotkey("ctrl","F5")
    
    

# Parkinson's Prediction Page
# if (selected == "Parkinsons Prediction"):

with tab3:
    
    with st.expander("What is Parkinson's Disease:"):
        st.write("A disorder of the central nervous system that affects movement, often including tremors.Nerve cell damage in the brain causes dopamine levels to drop, leading to the symptoms of Parkinson's.")
        
    with st.expander("Prerequisite tests needed to be done:"):
        st.write("1. MDVP Test")
        st.write("2. Jitter Test")
        st.write("3. Shimmer Test")
        
    with st.expander("How does our bot work:"):
        st.write("First you need to fill in all coloumns from the tests done earlier. Our expert Bot will analyse your metrics and then identifies if you have heart disease or not. Along with the result our expert bot will give you precautions to be followed and medication that needed to be taken.")
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, value=0.0, step=0.1)
        st.write(fo)
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, value=0.0, step=0.1)
        st.write(fhi)
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, value=0.0, step=0.1)
        st.write(flo)
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, value=0.0, step=0.1)
        st.write(Jitter_percent)
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, value=0.0, step=0.1)
        st.write(Jitter_Abs)
    with col1:
        RAP = st.number_input('MDVP:RAP', min_value=0.0, value=0.0, step=0.1)
        st.write(RAP)
    with col2:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0, value=0.0, step=0.1)
        st.write(PPQ)
    with col3:
        DDP = st.number_input('Jitter:DDP', min_value=0.0, value=0.0, step=0.1)
        st.write(DDP)
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, value=0.0, step=0.1)
        st.write(Shimmer)
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, value=0.0, step=0.1)
        st.write(Shimmer_dB)
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, value=0.0, step=0.1)
        st.write(APQ3)
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, value=0.0, step=0.1)
        st.write(APQ5)
    with col3:
        APQ = st.number_input('MDVP:APQ', min_value=0.0, value=0.0, step=0.1)
        st.write(APQ)
    with col4:
        DDA = st.number_input('Shimmer:DDA', min_value=0.0, value=0.0, step=0.1)
        st.write(DDA)
    with col5:
        NHR = st.number_input('NHR', min_value=0.0, value=0.0, step=0.1)
        st.write(NHR)
    with col1:
        HNR = st.number_input('HNR', min_value=0.0, value=0.0, step=0.1)
        st.write(HNR)
    with col2:
        RPDE = st.number_input('RPDE', min_value=0.0, value=0.0, step=0.1)
        st.write(RPDE)
    with col3:
        DFA = st.number_input('DFA', min_value=0.0, value=0.0, step=0.1)
        st.write(DFA)
    with col4:
        spread1 = st.number_input('spread1', min_value=0.0, value=0.0, step=0.1)
        st.write(spread1)
    with col5:
        spread2 = st.number_input('spread2', min_value=0.0, value=0.0, step=0.1)
        st.write(spread2)
    with col1:
        D2 = st.number_input('D2', min_value=0.0, value=0.0, step=0.1)
        st.write(D2)
    with col2:
        PPE = st.number_input('PPE', min_value=0.0, value=0.0, step=0.1)
        st.write(PPE)
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
          st.warning(parkinsons_diagnosis)
          with st.expander("Precautions "):
            st.write("rgrsf")
          with st.expander("Medications"):
              st.write("a")
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
          st.success(parkinsons_diagnosis)
        
    
    # if st.button('Reset all Parameters', key=16):
    #     pyautogui.hotkey("ctrl","F5")

