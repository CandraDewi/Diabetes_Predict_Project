import os # untuk operasi sistem (memeriksa lokasi file).
import pickle # untuk memuat model machine learning.
import pandas as pd # untuk pengolahan data tabular (csv, excel, dll).

# Membuat kelas Predictor yang akan menangani prediksi model machine learning.
class Predictor:
    # model_path -> lokasi file model.
    # csv_path -> lokasi file csv.
    def __init__(self, model_path="model/model.pkl", csv_path="diabetes use.csv"):
        
        #Memuat model machine learning dari file .pkl yang disimpan.
        # Memeriksa lokasi file model.
        if not os.path.exists(model_path): # Jika tidak ada maka program akan menampilkan pesan.
            print("Model tidak ditemukan. Melatih model baru...")

        #Membuka dan memuat model dari file .pkl yang disimpan   
        with open(model_path, "rb") as f: # file model dibuka dalam mode biner (rb) dengan nama variabel "f".
            # model akan dimuat menggunakan pickle.load(f) dan disimpan ke atribut self.model.. 
            self.model = pickle.load(f) 
    
    #Melakukan prediksi berdasarkan dataset
    def predict(self, df):
        return self.model.predict(df)
    
    #Melakukan prediksi hanya dengan 1 baris data
    def predict_single(self, input_data):
        # Mendeklarasikan nama-nama fitur yang diinginkan dalam model.
        feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                     'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        # Membuat dataframe dari data yang sudah diinputkan dengan nama kolom yang sesuai.
        df = pd.DataFrame(input_data, columns=feature_names)
        # Menggunakan model untuk memprediksi data tunggal.
        return self.model.predict(df)


