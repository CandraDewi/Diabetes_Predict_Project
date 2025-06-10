import os
import pickle
import pandas as pd


class Predictor:
    def __init__(self, model_path="model/model.pkl", csv_path="diabetes use.csv"):
        
        #Memuat model machine learning dari file .pkl yang disimpan.
        if not os.path.exists(model_path):
            print("Model tidak ditemukan. Melatih model baru...")

        #Membuka dan memuat model dari file .pkl yang disimpan   
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
    
    #Melakukan prediksi berdasarkan dataaset
    def predict(self, df):
        return self.model.predict(df)
    
    #Melakukan prediksi hanya dengan 1 baris data
    def predict_single(self, input_data):
        feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                     'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        df = pd.DataFrame(input_data, columns=feature_names)
        return self.model.predict(df)


