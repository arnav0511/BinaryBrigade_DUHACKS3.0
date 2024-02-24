# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn.preprocessing import LabelEncoder
import pickle
import pandas as pd

data=pd.read_csv('C:\\Users\\rushi\\OneDrive\\Desktop\\Minor\\Training.csv')
y=data['prognosis']

loaded_model=pickle.load(open('C:/Users/rushi/OneDrive/Desktop/Minor/trained_model.sav','rb'))

label_encoder=LabelEncoder()
encoded_labels=label_encoder.fit_transform(y)

input_data=[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
input_data=[input_data]
predictions=loaded_model.predict(input_data)
predicted_prognosis = label_encoder.inverse_transform(predictions)[0]
print("Predicted Prognosis:", predicted_prognosis)