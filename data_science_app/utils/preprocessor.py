#Data preprocessing
def preprocess_data(df):
    #Menhapus kolom outcome jika terdapat kolom outcome
    if 'Outcome' in df.columns:
        df = df.drop("Outcome", axis=1)

    #Jika ada missing value, maka akan diganti dengan nilai median
    columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in columns:
        df[col] = df[col].replace(0, df[col].median())
    
    return df
