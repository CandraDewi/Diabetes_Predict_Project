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
    if 'Outcome' not in df.columns:
        raise ValueError("Dataset harus memiliki kolom 'Outcome'.")

    #Split data antara fitur(x) dan target(y)
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']

    #Membuat dan melatih model dengan metode decisiontree
    model = DecisionTreeClassifier()
    model.fit(X, y)
    
    #Menyimpan model ke dalam folder "model" sebagai file .pkl
    os.makedirs("model", exist_ok=True)
    with open("model/model.pkl", "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    from ui.trainer_ui import run_trainer_ui
    run_trainer_ui()
