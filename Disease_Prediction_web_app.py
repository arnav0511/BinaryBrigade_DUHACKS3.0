from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pickle
import streamlit as st
import streamlit.components.v1 as com
import numpy as np

data=pd.read_csv('C:\\Users\\rushi\\OneDrive\\Desktop\\Minor\\Training.csv')
y=data['prognosis']

label_encoder=LabelEncoder()
encoded_labels=label_encoder.fit_transform(y)

loaded_model=pickle.load(open('C:/Users/rushi/OneDrive/Desktop/Minor/trained_model.sav','rb'))

symptom_descriptions = pd.read_csv('C:/Users/rushi/OneDrive/Desktop/Minor/symptom_Description.csv',names=['Disease', 'Description'])

symptom_precautions = pd.read_csv('C:/Users/rushi/OneDrive/Desktop/Minor/symptom_precaution.csv', names=['Disease', 'Precaution1', 'Precaution2', 'Precaution3', 'Precaution4'])
symptom_precautions[['Precaution1', 'Precaution2', 'Precaution3', 'Precaution4']] = symptom_precautions[['Precaution1', 'Precaution2', 'Precaution3', 'Precaution4']].astype(str)

symptom_descriptions = symptom_descriptions.set_index('Disease')['Description'].to_dict()

symptom_precautions_dict = symptom_precautions.set_index('Disease').to_dict(orient='index')

def disease_prediction(input_data):
    input_data=[input_data]
    predictions=loaded_model.predict(input_data)
    predicted_prognosis = label_encoder.inverse_transform(predictions)[0]
    description = symptom_descriptions.get(predicted_prognosis,"Description not found")
    precautions_info = symptom_precautions_dict.get(predicted_prognosis, {})
    precautions = [
        precautions_info.get('Precaution1', 'Precaution not available'),
        precautions_info.get('Precaution2', 'Precaution not available'),
        precautions_info.get('Precaution3', 'Precaution not available'),
        precautions_info.get('Precaution4', 'Precaution not available')
    ]
    precautions_str = '\n\n'.join(precautions)
    predicted_prognosis = predicted_prognosis.replace("_", " ")
    return f"Disease predicted: {predicted_prognosis}\n\nDescription: {description}\n\nPrecautions:\n\n{precautions_str}"

def main():
    com.html("""
             <div>
             <style>
             body{
                 display: flex;
                 align-items: center;
                 justify-content: center;
                 height: 100vh;
                 margin: 0;
            }
             h1.heading{
                 display: inline_block;
                 background-color: white;
                 font-family: "Open Sans", sans-serif;
                 color: black;
                 padding: 10px;
                 border-radius: 10px;
            }
             </style>
             <h1 class="heading">
             Consultiva
             </h1>
             </div>
             """)
    st.title("Disease Prediction")
    
    with open('C:/Users/rushi/OneDrive/Desktop/Minor/style.css') as f:
        css=f.read()
    
    st.markdown(f'<style>{css}<style>',unsafe_allow_html=True)
    
    # itching,skin_rash,nodal_skin_eruptions,continuous_sneezing,shivering,chills,joint_pain,stomach_pain,acidity,ulcers_on_tongue,muscle_wasting,vomiting,burning_micturition,spotting_ urination,fatigue,weight_gain,anxiety,cold_hands_and_feets,mood_swings,weight_loss,restlessness,lethargy,patches_in_throat,irregular_sugar_level,cough,high_fever,sunken_eyes,breathlessness,sweating,dehydration,indigestion,headache,yellowish_skin,dark_urine,nausea,loss_of_appetite,pain_behind_the_eyes,back_pain,constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine,yellowing_of_eyes,acute_liver_failure,fluid_overload,swelling_of_stomach,swelled_lymph_nodes,malaise,blurred_and_distorted_vision,phlegm,throat_irritation,redness_of_eyes,sinus_pressure,runny_nose,congestion,chest_pain,weakness_in_limbs,fast_heart_rate,pain_during_bowel_movements,pain_in_anal_region,bloody_stool,irritation_in_anus,neck_pain,dizziness,cramps,bruising,obesity,swollen_legs,swollen_blood_vessels,puffy_face_and_eyes,enlarged_thyroid,brittle_nails,swollen_extremeties,excessive_hunger,extra_marital_contacts,drying_and_tingling_lips,slurred_speech,knee_pain,hip_joint_pain,muscle_weakness,stiff_neck,swelling_joints,movement_stiffness,spinning_movements,loss_of_balance,unsteadiness,weakness_of_one_body_side,loss_of_smell,bladder_discomfort,foul_smell_of urine,continuous_feel_of_urine,passage_of_gases,internal_itching,toxic_look_(typhos),depression,irritability,muscle_pain,altered_sensorium,red_spots_over_body,belly_pain,abnormal_menstruation,dischromic _patches,watering_from_eyes,increased_appetite,polyuria,family_history,mucoid_sputum,rusty_sputum,lack_of_concentration,visual_disturbances,receiving_blood_transfusion,receiving_unsterile_injections,coma,stomach_bleeding,distention_of_abdomen,history_of_alcohol_consumption,fluid_overload,blood_in_sputum,prominent_veins_on_calf,palpitations,painful_walking,pus_filled_pimples,blackheads,scurring,skin_peeling,silver_like_dusting,small_dents_in_nails,inflammatory_nails,blister,red_sore_around_nose,yellow_crust_ooze
    symptoms = [
    "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering",
    "chills", "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue", "muscle_wasting",
    "vomiting", "burning_micturition", "spotting_urination", "fatigue", "weight_gain", "anxiety",
    "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness", "lethargy",
    "patches_in_throat", "irregular_sugar_level", "cough", "high_fever", "sunken_eyes",
    "breathlessness", "sweating", "dehydration", "indigestion", "headache", "yellowish_skin",
    "dark_urine", "nausea", "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "constipation",
    "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine", "yellowing_of_eyes",
    "acute_liver_failure", "fluid_overload", "swelling_of_stomach", "swelled_lymph_nodes",
    "malaise", "blurred_and_distorted_vision", "phlegm", "throat_irritation", "redness_of_eyes",
    "sinus_pressure", "runny_nose", "congestion", "chest_pain", "weakness_in_limbs",
    "fast_heart_rate", "pain_during_bowel_movements", "pain_in_anal_region", "bloody_stool",
    "irritation_in_anus", "neck_pain", "dizziness", "cramps", "bruising", "obesity",
    "swollen_legs", "swollen_blood_vessels", "puffy_face_and_eyes", "enlarged_thyroid",
    "brittle_nails", "swollen_extremeties", "excessive_hunger", "extra_marital_contacts",
    "drying_and_tingling_lips", "slurred_speech", "knee_pain", "hip_joint_pain",
    "muscle_weakness", "stiff_neck", "swelling_joints", "movement_stiffness",
    "spinning_movements", "loss_of_balance", "unsteadiness", "weakness_of_one_body_side",
    "loss_of_smell", "bladder_discomfort", "foul_smell_of urine", "continuous_feel_of_urine",
    "passage_of_gases", "internal_itching", "toxic_look_(typhos)", "depression", "irritability",
    "muscle_pain", "altered_sensorium", "red_spots_over_body", "belly_pain",
    "abnormal_menstruation", "dischromic_patches", "watering_from_eyes", "increased_appetite",
    "polyuria", "family_history", "mucoid_sputum", "rusty_sputum", "lack_of_concentration",
    "visual_disturbances", "receiving_blood_transfusion", "receiving_unsterile_injections",
    "coma", "stomach_bleeding", "distention_of_abdomen", "history_of_alcohol_consumption",
    "fluid_overload", "blood_in_sputum", "prominent_veins_on_calf", "palpitations",
    "painful_walking", "pus_filled_pimples", "blackheads", "scurring", "skin_peeling",
    "silver_like_dusting", "small_dents_in_nails", "inflammatory_nails", "blister",
    "red_sore_around_nose", "yellow_crust_ooze"]
    
    checkbox_values=np.zeros(len(symptoms),dtype=int)

    checkbox_container = st.container()

    # Display checkboxes in the container
    with checkbox_container:
        st.write("### Select the Symptoms")
        num_columns = 3
        columns = st.columns(num_columns)
        checkbox_values = []
        for i, symptom in enumerate(symptoms):
            symptom_with_space = symptom.replace("_", " ")
            checkbox_values.append(columns[i % num_columns].checkbox(symptom_with_space.capitalize(), key=f"{symptom}_{i}"))
        
    diagnosis=''

    if st.button('Predict'):
        diagnosis=disease_prediction(checkbox_values)
        
    st.success(diagnosis)
    
    
    
if __name__=='__main__':
    main()

    