import tkinter as tk
from tkinter import messagebox

class SinglePredictionForm:
    def __init__(self, root, predictor):
        # Mencegah window ganda
        if hasattr(root, 'predict_window') and root.predict_window.winfo_exists():
            tk.messagebox.showwarning("Peringatan", "Form prediksi masih terbuka.")
            return

        self.predict_window = tk.Toplevel(root)
        root.predict_window = self.predict_window  # Simpan referensi di root

        self.predict_window.title("Prediksi Data Individu")
        self.predict_window.geometry("400x550")
        self.predictor = predictor

        self.fields = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                       'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        self.entries = {}

        for i, field in enumerate(self.fields):
            label = tk.Label(self.predict_window, text=field)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(self.predict_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[field] = entry

        self.result_label = tk.Label(self.predict_window, text="", font=("Arial", 12, "bold"))
        self.result_label.grid(row=len(self.fields) + 2, column=0, columnspan=2, pady=10)

        submit_btn = tk.Button(self.predict_window, text="Prediksi", command=self.submit)
        submit_btn.grid(row=len(self.fields), column=0, pady=20, padx=10)

        clear_btn = tk.Button(self.predict_window, text="Clear", command=self.clear_entries)
        clear_btn.grid(row=len(self.fields), column=1, pady=20, padx=10)

    def submit(self):
        try:
            for field in self.fields:
                if self.entries[field].get() == "":
                    self.result_label.config(text="Semua form harus diisi.", fg="red")
                    return

            input_data = [float(self.entries[field].get()) for field in self.fields]
            prediction = self.predictor.predict_single([input_data])
            result = "Positif Diabetes" if prediction[0] == 1 else "Negatif Diabetes"
            self.result_label.config(text=f"Hasil: {result}", fg="green")
        except Exception as e:
            self.result_label.config(text=f"Input tidak valid: {e}", fg="red")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.result_label.config(text="")