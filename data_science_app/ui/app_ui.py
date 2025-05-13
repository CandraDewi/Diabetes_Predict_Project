import tkinter as tk # Modul GUI Python untuk membuat user interface
from tkinter import filedialog, messagebox, ttk # Komponen tambahan untuk dialog file, pesan pop-up, dan tabel
import pandas as pd # Untuk membaca dan mengelola data dalam bentuk tabel (CSV)
from model.predictor import Predictor # Mengimpor kelas Predictor untuk melakukan prediksi
from ui.predict_single_ui import SinglePredictionForm # Mengimpor form untuk prediksi data individu

# Membuat kelas utama aplikasi GUI untuk prediksi diabetes dengan dataset
class DataScienceApp:
    def __init__(self, root): # Konstruktor utama yang dijalankan saat objek dibuat
        self.root = root
        self.root.title("Prediksi Diabetes") # Judul jendela GUI
        self.root.geometry("800x600") # Ukuran jendela utama
        self.predictor = Predictor() # Memuat model prediktor dari file .pkl

        self.df = None # Menyimpan data yang diunggah
        self.predictions = None # Menyimpan hasil prediksi

        self.create_widgets() # Memanggil fungsi untuk menyiapkan tampilan interface

     # Membuat komponen-komponen user interface
    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Tombol untuk mengunggah dataset CSV
        self.load_button = tk.Button(frame, text="Upload Dataset CSV", command=self.load_csv)
        self.load_button.pack(side=tk.LEFT, padx=5)

        # Tombol untuk melakukan prediksi berdasarkan dataset
        self.predict_button = tk.Button(frame, text="Prediksi", command=self.predict, state=tk.DISABLED)
        self.predict_button.pack(side=tk.LEFT, padx=5)

        # Tombol untuk menyimpan hasil prediksi ke file CSV
        self.save_button = tk.Button(frame, text="Simpan Hasil ke CSV", command=self.save_results, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=5)

         # Tombol untuk membuka form prediksi satu baris data (data individu)
        self.single_btn = tk.Button(self.root, text="Prediksi Data Individu", command=self.open_single_prediction_form)
        self.single_btn.pack(pady=5)

        # Komponen Treeview untuk menampilkan isi dataset dan hasil prediksi
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(expand=True, fill=tk.BOTH, pady=10)


    # Fungsi untuk memuat file CSV dari pengguna
    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")]) # Dialog untuk memilih file
        if not file_path: # Jika pengguna membatalkan pemilihan file
            return
        try:
            self.df = pd.read_csv(file_path) # Membaca file CSV
            self.display_dataframe(self.df) # Menampilkan data di tabel GUI
            self.predict_button.config(state=tk.NORMAL) # Mengaktifkan tombol prediksi
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membaca file: {e}") # Menampilkan pesan error

    
    # Fungsi untuk melakukan prediksi pada seluruh dataset
    def predict(self):
        try:
            self.predictions = self.predictor.predict(self.df)  # Melakukan prediksi
            self.df["Predicted_Outcome"] = self.predictions  # Menambahkan kolom hasil prediksi
            self.display_dataframe(self.df) # Menampilkan hasil di tabel
            self.save_button.config(state=tk.NORMAL) # Mengaktifkan tombol simpan
        except Exception as e:
            messagebox.showerror("Error", f"Gagal melakukan prediksi: {e}") # Menampilkan pesan error jika gagal

    
    # Fungsi untuk menyimpan hasil prediksi ke file CSV
    def save_results(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        try:
            self.df.to_csv(file_path, index=False) # Menyimpan ke CSV tanpa menggunakan indeks
            messagebox.showinfo("Berhasil", "Hasil prediksi berhasil disimpan.") # Menampilkan pesan notifikasi jika sukses menyimpan
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan file: {e}") # Menampilkan pesan notifikasi jika gagal menyimpan

    
    # Fungsi untuk menampilkan dataframe (CSV) ke tabel (Treeview) di tampilan GUI
    def display_dataframe(self, df):
        self.tree.delete(*self.tree.get_children()) # Menghapus isi sebelumnya
        self.tree["columns"] = list(df.columns) # Menetapkan nama kolom
        self.tree["show"] = "headings"  # Menyembunyikan kolom indeks
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100) # Mengatur lebar kolom
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row)) # Menambahkan setiap baris ke Treeview

    
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

    # Fungsi untuk membuka form input prediksi satu baris data (data individu)
    def open_single_prediction_form(self):
        SinglePredictionForm(self.root, self.predictor) # Memanggil class/form dari file lain




