import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
import sys
import os

# Menambahkan path parent directory ke sys.path agar modul dari folder lain bisa diimpor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


#Melatih model DecisionTreeClassifier berdasarkan dataset CSV dan menyimpan model sebagai .pkl.
def train_and_save_model(file_path):
    df = pd.read_csv(file_path)
    # Memeriksa apakah kolom "Outcome" ada di dataset
    # Jika tidak ada, maka akan muncul error message.
    if 'Outcome' not in df.columns:
        raise ValueError("Dataset harus memiliki kolom 'Outcome'.")

    #Split data antara fitur(x) dan target(y)
    X = df.drop('Outcome', axis=1) # variabel x berisi semua kolom kecuali kolom Outcome (sebagai fitur prediktor).
    y = df['Outcome'] # variabel y berisi kolom outcome yang akan digunakan sebagai variabel target.

    #Membuat dan melatih model dengan metode decisiontree
    model = DecisionTreeClassifier()
    model.fit(X, y) # Melatih model menggunakan data X dan label y yang sudah dipisahkan sebelumnya
    
    #Menyimpan model ke dalam folder "model" sebagai file .pkl
    os.makedirs("model", exist_ok=True) # parameter exist_ok=True digunakan untuk mencegah error jika folder/directori sudah ada.
    # Membuka file "model/model.pkl" dalam mode write binary (wb) dengan nama variabel "f".
    with open("model/model.pkl", "wb") as f:
        # Menyimpan objek model ke file
        pickle.dump(model, f)

# Memastikan UI trainer dijalankan hanya jika file dieksekusi langsung bukan diimpor.
if __name__ == "__main__":
    # Jika dieksekusi langsung maka program akan mengimpor fungsi "ui.trainer_ui" dari modul "run_trainer_ui"
    from ui.trainer_ui import run_trainer_ui
    # Menjalankan UI untuk proses training
    run_trainer_ui()
