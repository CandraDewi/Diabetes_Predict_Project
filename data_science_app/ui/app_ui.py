import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
from model.predictor import Predictor
from ui.predict_single_ui import SinglePredictionForm

class DataScienceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prediksi Diabetes")
        self.root.geometry("800x600")
        self.predictor = Predictor()

        self.df = None
        self.predictions = None

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.load_button = tk.Button(frame, text="Upload Dataset CSV", command=self.load_csv)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.predict_button = tk.Button(frame, text="Prediksi", command=self.predict, state=tk.DISABLED)
        self.predict_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(frame, text="Simpan Hasil ke CSV", command=self.save_results, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.single_btn = tk.Button(self.root, text="Prediksi Data Individu", command=self.open_single_prediction_form)
        self.single_btn.pack(pady=5)

        self.tree = ttk.Treeview(self.root)
        self.tree.pack(expand=True, fill=tk.BOTH, pady=10)


    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        try:
            self.df = pd.read_csv(file_path)
            self.display_dataframe(self.df)
            self.predict_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membaca file: {e}")

    def predict(self):
        try:
            self.predictions = self.predictor.predict(self.df)
            self.df["Predicted_Outcome"] = self.predictions
            self.display_dataframe(self.df)
            self.save_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal melakukan prediksi: {e}")

    
    def save_results(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        try:
            self.df.to_csv(file_path, index=False)
            messagebox.showinfo("Berhasil", "Hasil prediksi berhasil disimpan.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan file: {e}")

    
    def display_dataframe(self, df):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    
    # def predict_single_row(self):
    #     if hasattr(self, 'predict_window') and self.predict_window.winfo_exists():
    #         tk.messagebox.showwarning("Peringatan", "Form prediksi masih terbuka.")
    #         return

    #     self.predict_window = tk.Toplevel(self.root)
    #     self.predict_window.title("Prediksi Data Individu")
    #     self.predict_window.geometry("400x550")

    #     fields = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
    #               'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    #     entries = {}

    #     for i, field in enumerate(fields):
    #         label = tk.Label(self.predict_window, text=field)
    #         label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    #         entry = tk.Entry(self.predict_window)
    #         entry.grid(row=i, column=1, padx=10, pady=5)
    #         entries[field] = entry

    #     result_label = tk.Label(self.predict_window, text="", font=("Arial", 12, "bold"))
    #     result_label.grid(row=len(fields) + 2, column=0, columnspan=2, pady=10)

    #     def submit():
    #         try:
    #             for field in fields:
    #                 if entries[field].get() == "":
    #                     result_label.config(text="Semua form harus diisi.", fg="red")
    #                     return
    #             input_data = [float(entries[field].get()) for field in fields]
    #             prediction = self.predictor.predict_single([input_data])
    #             result = "Positif Diabetes" if prediction[0] == 1 else "Negatif Diabetes"
    #             result_label.config(text=f"Hasil: {result}", fg="green")
    #         except Exception as e:
    #             result_label.config(text=f"Input tidak valid: {e}", fg="red")

    #     def clear_entries():
    #         for entry in entries.values():
    #             entry.delete(0, tk.END)
    #         result_label.config(text="")

    #     submit_btn = tk.Button(self.predict_window, text="Prediksi", command=submit)
    #     submit_btn.grid(row=len(fields), column=0, pady=20, padx=10)

    #     clear_btn = tk.Button(self.predict_window, text="Clear", command=clear_entries)
    #     clear_btn.grid(row=len(fields), column=1, pady=20, padx=10)

    def open_single_prediction_form(self):
        SinglePredictionForm(self.root, self.predictor)




