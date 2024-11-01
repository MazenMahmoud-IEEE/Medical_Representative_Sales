import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model and scaler
model = pickle.load(open("medical_representative.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Title of the app
st.title("Medical Representative Sales Prediction")
st.write("Predict whether a doctor is likely to prescribe our medicine.")

# Input fields
st.header("Enter Doctor Information")

# Doctor class
dr_class = st.selectbox("Doctor Class", ['A', 'B'])  # Assuming 'A' and 'B' represent the doctor classes

# Exam price
exam_price = st.number_input("Exam Price", min_value=0, max_value=1000, step=1)

# Medicine price
price = st.number_input("Medicine Price", min_value=0, max_value=1000, step=1)

# Area selection with simplified labels
area_labels = ['area1', 'area2', 'area3', 'area4', 'area5', 'area6', 'area7', 'area8']
area = st.selectbox("Area", area_labels)

# Speciality selection with simplified labels
speciality_labels = ['Cardiology', 'Chest', 'ENT', 'Gastroenterology', 'General Practice', 
                     'Internal Medicine', 'Neurology', 'Orthopedics', 'Surgery', 
                     'Urology', 'Vascular Surgery']
speciality = st.selectbox("Speciality", speciality_labels)

# Clinic/Hospital selection
clinic_hos = st.selectbox("Clinic or Hospital", ['Clinic', 'Hospital'])

# Medicine Type selection with simplified labels
medicine_type_labels = ['Type 1', 'Type 2', 'Type 3', 'Type 4', 'Type 5', 'Type 6']
medicine_type = st.selectbox("Medicine Type", medicine_type_labels)

# Process input into model features
input_data = {
    'dr_class': 1 if dr_class == 'A' else 0,
    'exam_price': exam_price,
    'price': price
}

# Encoding the selected area into the model's area feature columns
for i, area_option in enumerate(['area_area1', 'area_area2', 'area_area3', 'area_area4', 
                                 'area_area5', 'area_area6', 'area_area7', 'area_area8']):
    input_data[area_option] = 1 if area_labels[i] == area else 0

# Encoding the selected speciality into the model's speciality feature columns
speciality_options = ['speciality_cd', 'speciality_chest', 'speciality_ent', 'speciality_git', 
                      'speciality_gp', 'speciality_im', 'speciality_neuro', 'speciality_or', 
                      'speciality_sur', 'speciality_uro', 'speciality_vas']
for i, spec_option in enumerate(speciality_options):
    input_data[spec_option] = 1 if speciality_labels[i] == speciality else 0

# Encoding the clinic/hospital choice into the model's feature columns
input_data['clinic_hos_clinic'] = 1 if clinic_hos == 'Clinic' else 0
input_data['clinic_hos_hospital'] = 1 if clinic_hos == 'Hospital' else 0

# Encoding the selected medicine type into the model's medicine type feature columns
medicine_type_options = ['medicine_type1', 'medicine_type2', 'medicine_type3', 
                         'medicine_type4', 'medicine_type5', 'medicine_type6']
for i, med_type in enumerate(medicine_type_options):
    input_data[med_type] = 1 if medicine_type_labels[i] == medicine_type else 0

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Normalize only the exam_price and price
input_df_normalized = input_df.copy()
input_df_normalized[['exam_price', 'price']] = scaler.transform(input_df[['exam_price', 'price']])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df_normalized)
    if prediction == 1:
        st.error("Doctor is unlikely to prescribe the medicine.")
    else:
        st.success("Doctor is likely to prescribe the medicine.")
    #st.subheader(result)

