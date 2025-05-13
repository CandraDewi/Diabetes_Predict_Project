# Fungsi utama untuk melakukan preprocessing data
def preprocess_data(df):
    # Mengecek apakah kolom 'Outcome' ada di dalam data
    # Kalau ada, kolom 'Outcome' akan dihapus karena dianggap sebagai label (target)
    if 'Outcome' in df.columns:
        df = df.drop("Outcome", axis=1)

    # Jika ada missing value, maka akan diganti dengan nilai median
    columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in columns:
        df[col] = df[col].replace(0, df[col].median())
    
    # Setelah semua proses selesai, dataframe yang sudah diproses akan dikembalikan
    return df
