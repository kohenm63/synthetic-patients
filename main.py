import pandas as pd
from faker import Faker
import random
import streamlit as st
import numpy as np

fake = Faker()

def random_medical_history():
    medical_conditions = [
        "Hypertension", "Diabetes", "Hyperlipidemia", "Asthma", "Arthritis",
        "Coronary artery disease", "Congestive heart failure", "Chronic kidney disease",
        "Stroke", "Cancer", "Chronic obstructive pulmonary disease (COPD)", "Depression",
        "Anxiety disorder", "Thyroid disorder", "Gastroesophageal reflux disease (GERD)",
        "Peptic ulcer disease", "Gout", "Obesity", "Anemia", "Migraine", "Osteoporosis"
    ]
    history = random.sample(medical_conditions, random.randint(0, 5))  # Randomly select 0 to 5 medical conditions
    return history

common_allergies = [
    "Pollen", "Dust mites", "Mold spores", "Pet dander", "Food (Nuts, Dairy, Soy, Gluten)",
    "Insect stings", "Medications (Penicillin, Aspirin, Ibuprofen)", "Latex", "Metals (Nickel, Cobalt, Chromium)",
    "Fragrances", "Peanuts", "Shellfish", "Eggs", "Fish", "Wheat", "Sesame seeds",
    "Animal fur", "Bee stings", "Perfume", "Chemicals", "Grass", "Trees", "Cockroaches"
]

common_medications = [
    "Lisinopril", "Metformin", "Atorvastatin", "Levothyroxine", "Amlodipine", "Albuterol",
    "Hydrochlorothiazide", "Losartan", "Gabapentin", "Sertraline", "Acetaminophen", "Ibuprofen",
    "Simvastatin", "Omeprazole", "Amoxicillin", "Azithromycin", "Glipizide", "Warfarin",
    "Citalopram", "Insulin Glargine", "Aspirin", "Prednisone", "Fluoxetine", "Escitalopram"
]

education_levels = ["None", "High School/GED", "Associate's degree", "Bachelor's degree", "Master's degree", "Doctorate"]
marital_status = ["Single", "Married", "Divorced", "Widowed", "Separated"]
lifestyle_choices = ["Non-smoker", "Smoker", "Occasional drinker", "Regular drinker", "Vegetarian", "Vegan", "Regular exercise", "No exercise"]

def create_patient_data(num):
    patients = []
    for _ in range(num):
        patient = {
            'ID': fake.unique.random_number(digits=5),
            'Name': fake.name(),
            'Age': fake.random_int(min=1, max=100),
            'Address': fake.address(),
            'Blood Type': random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']),
            'Gender': random.choice(['Male', 'Female', 'Other']),
            'Allergies': ', '.join(random.sample(common_allergies, random.randint(0, 5))),
            'Medications': ', '.join(random.sample(common_medications, random.randint(1, 3))),
            'Insurance': random.choice(["Insured - Plan A", "Insured - Plan B", "Uninsured", None]),
            'Ethnic Background': random.choice(['Caucasian', 'Hispanic', 'African American', 'Asian']),
            'Occupation': random.choice(['Teacher', 'Engineer', 'Healthcare Worker', 'Clerk', 'Unemployed']),
            'Insurance Status': random.choice(['Insured', 'Underinsured', 'Uninsured']),
            'Marital Status': random.choice(marital_status),
            'Lifestyle': ', '.join(random.sample(lifestyle_choices, random.randint(1, 3))),
            'Medical History': ', '.join(random_medical_history()),  # Generate random medical history
            'Vital Signs': {
                'BP': f"{np.random.randint(110, 150)}/{np.random.randint(70, 90)}",
                'HR': random.randint(60, 100),
                'RR': random.randint(12, 30),
                'Temp': round(random.uniform(97.0, 100.0), 1),
            }
        }
        patients.append(patient)
    return pd.DataFrame(patients)

# Define a USMLE-style question
question = "What is the most likely diagnosis for a patient with severe chest pain, sweating, and nausea?"
options = ["Acute myocardial infarction", "Gastroesophageal reflux disease", "Panic attack", "Pneumonia"]
correct_answer = options[0]  # "Acute myocardial infarction" is the correct answer

# Streamlit app setup
st.title('Patient Synthetic Data 🏥')
st.write('This web app displays patient data.')

# Create a DataFrame with 10 dummy patients
df_patients = create_patient_data(10)

# Display the dataframe
st.dataframe(df_patients)

