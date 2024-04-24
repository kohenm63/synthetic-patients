import pandas as pd
import random
import streamlit as st
import numpy as np
from faker import Faker

fake = Faker()

# Define disease lists based on age categories
young_adult_conditions = [
    "Asthma", "Type 1 Diabetes", "Anxiety disorder", "Depression", "Acne",
    # Add 100 more conditions
    "Allergic rhinitis", "Menstrual disorders", "Sports injuries", "Mononucleosis",
    "Irritable bowel syndrome", "Chronic fatigue syndrome", "Eating disorders",
    "Substance abuse", "Attention deficit hyperactivity disorder (ADHD)", "Migraines",
    "Sexually transmitted infections (STI)", "Acute bronchitis", "Influenza",
    "Tonsillitis", "Anemia", "Varicella (Chickenpox)", "Mumps", "Rubella",
    "Human papillomavirus (HPV)", "Gastritis", "Ulcerative colitis", "Crohn's disease",
    "Acute sinusitis", "Dental caries", "Periodontal diseases", "Orthopedic injuries",
    "Hearing loss", "Visual impairments", "Psoriasis", "Eczema", "Tinea infections",
    "Scabies", "Lyme disease", "Hepatitis A", "Hepatitis B", "Hepatitis C",
    "Tuberculosis", "Pneumonia", "Amebiasis", "Giardiasis", "Candidiasis",
    "Urinary tract infections", "Appendicitis", "Concussions", "Burns",
    "Electric shock", "Fractures", "Dislocations", "Sprains", "Strains",
    "Contusions", "Lacerations", "Insect bites", "Animal bites", "Hypoglycemia",
    "Hyperglycemia", "Heat stroke", "Heat exhaustion", "Sunburn", "Hypothermia",
    "Frostbite", "Drowning", "Near drowning", "Electrocution", "Radiation sickness",
    "Smoke inhalation", "Chemical burns", "Poisoning", "Drug overdose", "Alcohol poisoning",
    "Carbon monoxide poisoning", "Food poisoning", "Choking", "Suffocation", "Asphyxiation",
    "Traumatic brain injury", "Spinal cord injury", "Nerve damage", "Arterial embolism",
    "Venous thrombosis", "Hyperthyroidism", "Hypothyroidism", "Diabetic ketoacidosis",
    "Hyperosmolar hyperglycemic state", "Endocarditis", "Myocarditis", "Pericarditis",
    "Sepsis", "Septic shock", "Rhabdomyolysis", "Electrolyte imbalances", "Dehydration",
    "Malnutrition", "Obesity", "Anorexia nervosa", "Bulimia nervosa", "Binge eating disorder"
]

middle_aged_conditions = [
    "Type 2 Diabetes", "Hypertension", "Hyperlipidemia", "Cancer", "Chronic kidney disease",
    "Coronary artery disease",
    # Add 100 more conditions
    "Peripheral artery disease", "Venous thromboembolism", "Aortic aneurysm", "Heart arrhythmias",
    "Cardiomyopathy", "Liver cirrhosis", "Non-alcoholic fatty liver disease", "Cholelithiasis",
    "Peptic ulcer disease", "Hepatic steatosis", "Chronic pancreatitis", "Osteoarthritis",
    "Rheumatoid arthritis", "Gout", "Fibromyalgia", "Spondylopathies", "Interstitial lung disease",
    "Sleep apnea", "Chronic bronchitis", "Emphysema", "Pulmonary hypertension", "Deep vein thrombosis",
    "Pulmonary embolism", "Benign prostatic hyperplasia", "Prostate cancer", "Breast cancer",
    "Colon cancer", "Cervical cancer", "Endometrial cancer", "Ovarian cancer", "Pancreatic cancer",
    "Thyroid cancer", "Melanoma", "Non-Hodgkin lymphoma", "Hodgkin lymphoma", "Leukemia",
    "Multiple myeloma", "Sarcoma", "Kidney cancer", "Bladder cancer", "Esophageal cancer",
    "Gastric cancer", "Liver cancer", "Laryngeal cancer", "Pharyngeal cancer", "Oral cancer",
    "Skin cancer", "Testicular cancer", "Adrenal cancer", "Parathyroid cancer", "Pituitary cancer",
    "Brain tumors", "Neurological disorders", "Multiple sclerosis", "Parkinson's disease",
    "Alzheimer's disease", "Huntington's disease", "Epilepsy", "Stroke", "Transient ischemic attack",
    "Dementia", "Delirium", "Bipolar disorder", "Schizophrenia", "Obsessive-compulsive disorder",
    "Panic disorder", "Post-traumatic stress disorder (PTSD)", "Generalized anxiety disorder",
    "Major depressive disorder", "Dysthymia", "Addiction disorders", "Alcohol dependence",
    "Drug dependence", "Nicotine dependence", "Metabolic syndrome", "Dyslipidemia",
    "Hypercholesterolemia", "Hypertriglyceridemia", "Hypothyroidism", "Hyperthyroidism",
    "Cushing's syndrome", "Addison's disease", "Grave's disease", "Hashimoto's thyroiditis",
    "Diabetic neuropathy", "Diabetic retinopathy", "Diabetic nephropathy", "Urolithiasis",
    "Urinary incontinence", "Sexual dysfunction", "Impotence", "Infertility", "Polycystic ovary syndrome",
    "Endometriosis", "Menopause", "Andropause", "Osteopenia", "Osteoporosis", "Calcium deficiency",
    "Iron deficiency anemia", "Vitamin D deficiency", "Vitamin B12 deficiency", "Folic acid deficiency"
]

elderly_conditions = [
    "Dementia", "Osteoporosis", "Stroke", "Congestive heart failure", "Arthritis",
    "Macular degeneration",
    # Add 100 more conditions
    "Senile cataracts", "Glaucoma", "Age-related hearing loss", "Presbyopia", "Dry eye syndrome",
    "Diabetic retinopathy", "Age-related macular degeneration", "Vascular dementia", "Lewy body dementia",
    "Parkinson's disease", "Alzheimer's disease", "Frontotemporal dementia", "Amyotrophic lateral sclerosis",
    "Multiple sclerosis", "Chronic obstructive pulmonary disease", "Idiopathic pulmonary fibrosis",
    "Pneumonia", "Influenza", "Herpes zoster (shingles)", "Urinary tract infections", "Sepsis",
    "Bacterial infections", "Viral infections", "Fungal infections", "Parasitic infections",
    "Prostatic hyperplasia", "Prostate cancer", "Bladder cancer", "Kidney failure", "Hepatic failure",
    "Cardiac failure", "Atrial fibrillation", "Cardiac arrhythmias", "Valvular heart disease",
    "Peripheral vascular disease", "Venous insufficiency", "Deep vein thrombosis", "Pulmonary embolism",
    "Varicose veins", "Orthostatic hypotension", "Syncope", "Falls", "Fractures", "Joint dislocations",
    "Muscle atrophy", "Sarcopenia", "Lipid disorders", "Hypertension", "Type 2 diabetes",
    "Metabolic syndrome", "Obesity", "Malnutrition", "Vitamin deficiencies", "Mineral deficiencies",
    "Dehydration", "Electrolyte imbalances", "Renal insufficiency", "Liver cirrhosis", "Gallstones",
    "Gastroesophageal reflux disease", "Peptic ulcer disease", "Colorectal cancer", "Pancreatic cancer",
    "Stomach cancer", "Esophageal cancer", "Oral cancer", "Throat cancer", "Lung cancer",
    "Mesothelioma", "Asbestosis", "Radiation-induced cancers", "Chemotherapy side effects",
    "Radiation therapy side effects", "Immunosenescence", "Autoimmune disorders", "Rheumatoid arthritis",
    "Psoriatic arthritis", "Systemic lupus erythematosus", "Gout", "Fibromyalgia", "Chronic pain syndromes",
    "Neuropathic pain", "Cognitive decline", "Memory loss", "Attention deficits", "Sleep disorders",
    "Insomnia", "Sleep apnea", "Restless legs syndrome", "Night terrors", "Depressive disorders",
    "Anxiety disorders", "Mood disorders", "Schizophrenia", "Delusional disorders", "Hallucinations"
]

# Define general medical conditions
general_conditions = [
    "Hypertension", "Diabetes", "Hyperlipidemia", "Asthma", "Arthritis",
    "Coronary artery disease", "Congestive heart failure", "Chronic kidney disease",
    "Stroke", "Cancer", "Chronic obstructive pulmonary disease (COPD)", "Depression",
    "Anxiety disorder", "Thyroid disorder", "Gastroesophageal reflux disease (GERD)"
    # Add 100 more general conditions
    "Acute bronchitis", "Allergic rhinitis", "Anemia", "Angina pectoris", "Aortic aneurysm",
    "Appendicitis", "Arrhythmias", "Arteriosclerosis", "Asthmatic bronchitis", "Atrial fibrillation",
    "Autism spectrum disorders", "Autoimmune diseases", "Bacterial infections", "Benign prostatic hyperplasia",
    "Bipolar disorder", "Bladder infections", "Bone fractures", "Bronchial asthma", "Bronchiectasis",
    "Bronchiolitis", "Bronchitis", "Bulimia nervosa", "Burns", "Bursitis", "Candidiasis",
    "Carpal tunnel syndrome", "Cataracts", "Celiac disease", "Cerebral palsy", "Cervical cancer",
    "Chickenpox", "Chlamydia infections", "Cholera", "Cholelithiasis", "Chronic bronchitis",
    "Chronic fatigue syndrome", "Chronic liver disease", "Chronic lymphocytic leukemia", "Chronic myeloid leukemia",
    "Chronic pancreatitis", "Chronic renal failure", "Cirrhosis of the liver", "Colitis", "Colon cancer",
    "Colorectal cancer", "Congenital heart defects", "Conjunctivitis", "COPD", "Crohn's disease",
    "Croup", "Cushing's syndrome", "Cystic fibrosis", "Cystitis", "Dengue fever", "Dental caries",
    "Depressive disorders", "Dermatitis", "Diabetic nephropathy", "Diabetic neuropathy", "Diabetic retinopathy",
    "Diarrhea", "Diverticulitis", "Diverticulosis", "Dizziness", "Down syndrome", "Drug addiction",
    "Dysentery", "Dyslipidemia", "Dyspepsia", "Ear infections", "Eating disorders", "Eczema",
    "Emphysema", "Encephalitis", "Endocarditis", "Endometrial cancer", "Endometriosis", "Epilepsy",
    "Erectile dysfunction", "Esophageal cancer", "Esophagitis", "Eye infections", "Fatty liver disease",
    "Fibrocystic breast disease", "Fibroids", "Fibromyalgia", "Food allergies", "Food poisoning",
    "Gallbladder disease", "Gallstones", "Gangrene", "Gastric cancer", "Gastritis", "Gastroenteritis",
    "Gastroesophageal reflux disease (GERD)", "Genital herpes", "Genital warts", "Giardiasis",
    "Gingivitis", "Glaucoma", "Gonorrhea", "Gout", "Graves' disease", "Guillain-Barré syndrome",
    "Gum diseases", "Haemophilia", "Hair loss", "Hashimoto's thyroiditis", "Hay fever", "Headaches",
    "Heart attacks", "Heart disease", "Heart failure", "Helicobacter pylori infection", "Hemochromatosis",
    "Hemorrhoids", "Hepatitis A", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E",
    "Herpes simplex virus", "Hiatal hernia", "High cholesterol", "HIV/AIDS", "Hives", "Hodgkin's lymphoma",
    "Hormonal imbalances", "Human papillomavirus (HPV)", "Huntington's disease", "Hypercholesterolemia",
    "Hyperkalemia", "Hyperlipidemia", "Hypertension", "Hyperthyroidism", "Hypoglycemia", "Hypothyroidism",
    "Idiopathic thrombocytopenic purpura (ITP)", "Impetigo", "Indigestion", "Infertility", "Inflammatory bowel disease (IBD)",
    "Influenza", "Inguinal hernia", "Insomnia", "Interstitial cystitis", "Interstitial lung disease", "Intestinal obstructions",
    "Irritable bowel syndrome (IBS)", "Jaundice", "Joint dislocations", "Juvenile diabetes", "Kidney cancer", "Kidney diseases",
    "Kidney infections", "Kidney stones", "Knee pain", "Lactose intolerance", "Laryngitis", "Lead poisoning",
    "Learning disabilities", "Legionnaires' disease", "Leukemia", "Lichen planus", "Lichen sclerosus", "Liver cancer",
    "Liver disease", "Lou Gehrig's disease (ALS)", "Low blood pressure", "Low blood sugar", "Lung cancer", "Lupus",
    "Lyme disease", "Lymphedema", "Lymphoma", "Macular degeneration", "Malaria", "Malnutrition", "Measles",
    "Melanoma", "Meningitis", "Menopause", "Menstrual cramps", "Mental health disorders", "Migraines", "Mitral valve prolapse",
    "Mononucleosis", "Mood disorders", "Mouth cancer", "Multiple myeloma", "Multiple sclerosis", "Mumps",
    "Muscular dystrophy", "Myasthenia gravis", "Myelodysplastic syndromes", "Myocardial infarction", "Myopia",
    "Nail fungus", "Narcolepsy", "Nasal polyps", "Nephritis", "Nerve damage", "Neuralgia", "Neuritis",
    "Neuroblastoma", "Neurofibromatosis", "Neuropathy", "Nicotine dependence", "Non-Hodgkin's lymphoma", "Norovirus infection",
    "Nosebleeds", "Obesity", "Obsessive-compulsive disorder (OCD)", "Osteoarthritis", "Osteomalacia", "Osteomyelitis",
    "Osteopenia", "Osteoporosis", "Otitis media", "Ovarian cancer", "Ovarian cysts", "Overactive bladder", "Pain management",
    "Pancreatic cancer", "Pancreatitis", "Panic disorder", "Parkinson's disease", "Pelvic inflammatory disease (PID)", "Peptic ulcer",
    "Pericarditis", "Periodontal disease", "Peripheral artery disease", "Peripheral neuropathy", "Peritonitis", "Pertussis",
    "Pheochromocytoma", "Phlebitis", "Pilonidal cyst", "Pituitary tumors", "Plague", "Plantar fasciitis", "Pleurisy",
    "Pneumococcal disease", "Pneumonia", "Poison ivy", "Poison oak", "Poisoning", "Polio", "Polycystic kidney disease",
    "Polycystic ovary syndrome (PCOS)", "Polymyalgia rheumatica", "Polyps", "Postpartum depression", "Post-traumatic stress disorder (PTSD)",
    "Pre-eclampsia", "Pregnancy", "Premature ejaculation", "Premenstrual syndrome (PMS)", "Presbyopia", "Progeria",
    "Prolapsed disc", "Prostate cancer", "Prostatitis", "Psoriasis", "Psoriatic arthritis", "Psychosis", "Pulmonary edema",
    "Pulmonary embolism", "Pulmonary fibrosis", "Pulmonary hypertension", "Rabies", "Radiation sickness", "Raynaud's phenomenon",
    "Rectal cancer", "Reflux", "Reiter's syndrome", "Renal failure", "Restless legs syndrome", "Retinitis pigmentosa",
    "Rheumatic fever", "Rheumatoid arthritis", "Rickets", "Ringworm", "Rosacea", "Rotavirus", "Rubella",
    "Salmonella infection", "Sarcoidosis", "Scabies", "Scarlet fever", "Schizophrenia", "Scleroderma", "Scoliosis",
    "Seasonal affective disorder (SAD)", "Seborrheic dermatitis", "Seizures", "Sepsis", "Septicemia", "Sexual dysfunction",
    "Shigellosis", "Shingles", "Sickle cell anemia", "Sinusitis", "Sjogren's syndrome", "Skin cancer", "Skin infections",
    "Sleep apnea", "Sleep disorders", "Small intestine cancer", "Smallpox", "Smoking cessation", "Snoring", "Social anxiety disorder",
    "Soft tissue sarcoma", "Spina bifida", "Spinal cord injuries", "Spinal stenosis", "Spleen disorders", "Spondylitis",
    "Sports injuries", "Sprains and strains", "Staphylococcal infections", "Stomach cancer", "Stomach ulcers", "Strep throat",
    "Stress", "Stroke", "Stuttering", "Subarachnoid hemorrhage", "Subdural hematoma", "Sudden infant death syndrome (SIDS)",
    "Suicide", "Sunburn", "Supraventricular tachycardia", "Swine flu (H1N1)", "Syphilis", "Systemic lupus erythematosus (SLE)",
    "Tachycardia", "Tardive dyskinesia", "Tay-Sachs disease", "Teeth grinding (bruxism)", "Temporal arteritis", "Tendonitis",
    "Tennis elbow", "Testicular cancer", "Tetanus", "Thalassemia", "Thoracic outlet syndrome", "Throat cancer", "Thrombocytopenia",
    "Thrombophlebitis", "Thrombosis", "Thyroid cancer", "Thyroid disorders", "Tinnitus", "Tonsillitis", "Tooth decay",
    "Tooth infections", "Tourette syndrome", "Toxic shock syndrome", "Tracheitis", "Transient ischemic attack (TIA)",
    "Transplant rejection", "Traumatic brain injury", "Traveler's diarrhea", "Tremors", "Trichomoniasis", "Trigeminal neuralgia",
    "Tuberculosis", "Tularemia", "Type 1 diabetes", "Type 2 diabetes", "Ulcerative colitis", "Ulcers", "Umbilical hernia",
    "Undescended testicle", "Urinary incontinence", "Urinary tract infections (UTI)", "Urticaria", "Uterine cancer", "Uterine fibroids",
    "Uterine prolapse", "Vaginal cancer", "Vaginal infections", "Varicella (chickenpox)", "Varicose veins", "Vascular dementia",
    "Vasculitis", "Venous insufficiency", "Venous thromboembolism", "Vertigo", "Viral hepatitis", "Viral infections", "Vitamin B12 deficiency",
    "Vitamin D deficiency", "Vitiligo", "Vocal cord nodules", "Von Willebrand disease", "Vulvar cancer", "Waldenstrom's macroglobulinemia",
    "Warts", "West Nile virus", "Whiplash", "Whooping cough", "Wilson's disease", "Wolff-Parkinson-White syndrome", "Wound infections",
    "Wrinkles", "Xeroderma pigmentosum", "Yellow fever", "Zika virus", "Zollinger-Ellison syndrome"
]
common_medications = [
    "Lisinopril", "Metformin", "Atorvastatin", "Levothyroxine", "Amlodipine", "Albuterol",
    "Hydrochlorothiazide", "Losartan", "Gabapentin", "Sertraline", "Acetaminophen", "Ibuprofen",
    "Simvastatin", "Omeprazole", "Amoxicillin", "Azithromycin", "Glipizide", "Warfarin",
    "Citalopram", "Insulin Glargine", "Aspirin", "Prednisone", "Fluoxetine", "Escitalopram",
    "Venlafaxine", "Trazodone", "Ranitidine", "Furosemide", "Cetirizine", "Diphenhydramine",
    "Sulfamethoxazole-Trimethoprim", "Cyclobenzaprine", "Methylprednisolone", "Pantoprazole",
    "Meloxicam", "Clonazepam", "Clopidogrel", "Bupropion", "Duloxetine", "Loratadine",
    "Fluticasone", "Testosterone", "Naproxen", "Valacyclovir", "Finasteride", "Vitamin D3",
    "Tamsulosin", "Hydroxyzine", "Oxycodone", "Lisinopril-Hydrochlorothiazide",
    "Esomeprazole", "Ethanol", "Sildenafil", "Tadalafil", "Carvedilol", "Aripiprazole",
    "Levofloxacin", "Latanoprost", "Methotrexate", "Thyroid", "Ramipril", "Spironolactone",
    "Triamterene-Hydrochlorothiazide", "Bisoprolol", "Digoxin", "Enalapril", "Varenicline",
    "Isosorbide Mononitrate", "Chlorthalidone", "Clarithromycin", "Ciprofloxacin",
    "Nortriptyline", "Lithium", "Phenytoin", "Nitroglycerin", "Amiodarone", "Glyburide",
    "Diclofenac", "Celecoxib", "Allopurinol", "Propofol", "Ketorolac", "Morphine",
    "Hydromorphone", "Benzonatate", "Fenofibrate", "Rosuvastatin", "Pravastatin",
    "Niacin", "Exenatide", "Liraglutide", "Sitagliptin", "Canagliflozin", "Pioglitazone",
    "Vildagliptin", "Empagliflozin", "Insulin Detemir", "Insulin Aspart", "Sevoflurane",
    "Isoflurane", "Haloperidol", "Risperidone", "Lamotrigine", "Olanzapine"
]
common_allergies = [
    "Pollen", "Dust mites", "Mold spores", "Pet dander", "Food (Nuts, Dairy, Soy, Gluten)",
    "Insect stings", "Medications (Penicillin, Aspirin, Ibuprofen)", "Latex", "Metals (Nickel, Cobalt, Chromium)",
    "Fragrances", "Peanuts", "Shellfish", "Eggs", "Fish", "Wheat", "Sesame seeds",
    "Animal fur", "Bee stings", "Perfume", "Chemicals", "Grass", "Trees", "Cockroaches"
]
lifestyle_choices = ["Non-smoker", "Smoker", "Occasional drinker", "Regular drinker", "Vegetarian", "Vegan", "Regular exercise", "No exercise"]


def random_medical_history(age):
    if age < 30:
        base_conditions = young_adult_conditions
    elif age < 60:
        base_conditions = middle_aged_conditions
    else:
        base_conditions = elderly_conditions
    
    # Combine age-specific and general conditions
    final_conditions = random.sample(base_conditions, min(len(base_conditions), random.randint(1, 3))) + \
                       random.sample(general_conditions, min(len(general_conditions), random.randint(0, 2)))
    return random.sample(final_conditions, min(len(final_conditions), random.randint(0, 5)))

def create_patient_data(num):
    patients = []
    for _ in range(num):
        age = fake.random_int(min=18, max=120)
        min_fahrenheit = 97.0
        max_fahrenheit = 100.0
        min_celsius = (min_fahrenheit - 32) * 5 / 9
        max_celsius = (max_fahrenheit - 32) * 5 / 9
        patient = {
            'ID': fake.unique.random_number(digits=5),
            'Name': fake.name(),
            'Age': age,
            'Address': fake.address(),
            'Blood Type': random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']),
            'Gender': random.choice(['Male', 'Female', 'Other']),
            'Allergies': ', '.join(random.sample(common_allergies, random.randint(0, 5))),
            'Medications': ', '.join(random.sample(common_medications, random.randint(1, 3))),
            'Insurance': random.choice(["Insured - Plan A", "Insured - Plan B", "Uninsured"]),
            'Ethnic Background': random.choice(['Caucasian', 'Hispanic', 'African American', 'Asian']),
            'Occupation': random.choice(['Teacher', 'Engineer', 'Healthcare Worker', 'Clerk', 'Unemployed']),
            'Insurance Status': random.choice(['Insured', 'Underinsured', 'Uninsured']),
            'Marital Status': random.choice(['Single', 'Married', 'Divorced', 'Widowed', 'Separated']),
            'Lifestyle': ', '.join(random.sample(lifestyle_choices, random.randint(1, 3))),
            'Medical History': ', '.join(random_medical_history(age)),
            'Vital Signs': {
                'BP': f"{np.random.randint(100, 150)}/{np.random.randint(60, 90)}",
                'HR': random.randint(60, 100),
                'RR': random.randint(12, 30),
                'Temp':round(random.uniform(min_celsius, max_celsius), 1),
                'Sat': random.randint(90, 100)

            }
        }
        patients.append(patient)
    return pd.DataFrame(patients)


def apply_filters(df, age_range, gender, condition):
    filtered_df = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]
    if gender != 'All':
        filtered_df = filtered_df[filtered_df['Gender'] == gender]
    if condition:
        filtered_df = filtered_df[filtered_df['Medical History'].str.contains(condition, case=False, na=False)]
    return filtered_df    



# Streamlit app setup
st.title('Adult Patients Synthetic Data 🏥')
st.write('This web app displays fake patient data.')


# # Create a DataFrame with 10 dummy patients
# df_patients = create_patient_data(10)

# # Display the dataframe
# st.dataframe(df_patients)
# ####################################################################
# st.sidebar.header('Generate Patient Data')

# Sidebar for data generation
st.sidebar.header('Filter Patient Data')
num_patients = st.sidebar.slider('Number of Patients', 10, 100, 10, step=10)


# Sidebar for filters
st.sidebar.header('Filter Options')
min_age, max_age = st.sidebar.slider('Select Age Range', 18, 120, (25, 75))
gender_options = ['All', 'Male', 'Female', 'Other']
gender = st.sidebar.selectbox('Select Gender', gender_options)
medical_condition = st.sidebar.text_input('Search for medical conditions')

if st.sidebar.button('Generate'):
    df_patients = create_patient_data(num_patients)
    filtered_data = apply_filters(df_patients, (min_age, max_age), gender, medical_condition)
    st.dataframe(filtered_data)
else:
    st.write("Use the controls to generate and filter the data.")
