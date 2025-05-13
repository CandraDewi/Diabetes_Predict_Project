import tkinter as tk # Untuk membuat aplikasi GUI (Graphical User Interface).
from tkinter import messagebox # Untuk menampilkan dialog box ke user.

# Membuat kelas untuk memprediksi data individu
class SinglePredictionForm:
    # root -> window utama aplikasi.
    # predictior -> objek predictor yang sudah dibuat sebelumnya.
    def __init__(self, root, predictor):
        # Mencegah window ganda
        # Memeriksa apakah window prediksi sudah dibuka sebelumnya.
        if hasattr(root, 'predict_window') and root.predict_window.winfo_exists():
            # Jika window sudah ada, maka program akan menampilkan peringatan dan menghentikan pembuatan form baru.
            tk.messagebox.showwarning("Peringatan", "Form prediksi masih terbuka.") 
            return
        # Inisialisasi window prediksi
        self.predict_window = tk.Toplevel(root) # Toplevel -> membuat window sekunder diatas window utama.
        root.predict_window = self.predict_window  # Simpan referensi di root

        # Menentukan judul dan ukuran window
        self.predict_window.title("Prediksi Data Individu") # judul window
        self.predict_window.geometry("400x550") # ukuran window
        self.predictor = predictor # Menyimpan objek predictor untuk digunakan saat melakukan prediksi.

        # Mendefinisikan daftar field sesuai dengan fitur model diabetes.
        self.fields = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                       'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        # Membuat dictionary kosong untuk menyimpan entry widget
        self.entries = {}

        # Membuat form input
        for i, field in enumerate(self.fields):
            label = tk.Label(self.predict_window, text=field)
            # Mengatur layout
            # sticky="w" -> label rata kiri (west).
            # padx -> spasi horizontal (samping/ kanan-kiri) || pady -> spasi vertikal (atas-bawah)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w") # nama parameter di kolom 0.
            entry = tk.Entry(self.predict_window) # Membuat widget "entry" (entry text) untuk diinput user.
            # Mengatur layout
            # padx -> spasi horizontal (samping/ kanan-kiri) || pady -> spasi vertikal (atas-bawah)
            entry.grid(row=i, column=1, padx=10, pady=5) # entry/ input field (untuk inputan user) di kolom 1.
            # Menyimpan referensi ke semua input field dengan nama variabel "entry".
            self.entries[field] = entry

        # Hasil prediksi
        # Membuat label kosong untuk menampilkan hasil prediksi
        self.result_label = tk.Label(self.predict_window, text="", font=("Arial", 12, "bold"))
        # Hasil prediksi akan muncul di bawah form
        self.result_label.grid(row=len(self.fields) + 2, column=0, columnspan=2, pady=10)
        
        # Membuat tombol "Prediksi" yang akan memanggil method "submit()".
        # Untuk memuat hasil prediksi 
        submit_btn = tk.Button(self.predict_window, text="Prediksi", command=self.submit)
        # Tombol berada di bawah semua field (kolom 0)
        submit_btn.grid(row=len(self.fields), column=0, pady=20, padx=10)

        # Membuat tombol "Clear" yang akan memanggil method "clear_entries()" saat di klik.
        # Untuk menghapus semua inputan user di kolom entry.
        clear_btn = tk.Button(self.predict_window, text="Clear", command=self.clear_entries)
        # Tombol berada di bawah semua field (kolom 1)
        clear_btn.grid(row=len(self.fields), column=1, pady=20, padx=10)
        
    # Method submit untuk prediksi
    # Dijalankan ketika tombol "Submit" di klik.
    def submit(self):
        try:
            # Memeriksa semua fields
            for field in self.fields:
                # Jika ada field yang kosong maka akan muncul error message dan proses akan dihentikan.
                if self.entries[field].get() == "":
                    self.result_label.config(text="Semua form harus diisi.", fg="red")
                    return

            # Mengubah semua inputan dengan tipe data string menjadi float
            input_data = [float(self.entries[field].get()) for field in self.fields]
            prediction = self.predictor.predict_single([input_data])
            # Menentukan hasil prediksi, 1 = Positif, 0 =  Negatif.
            result = "Positif Diabetes" if prediction[0] == 1 else "Negatif Diabetes"
            # Menampilkan hasil prediksi
            self.result_label.config(text=f"Hasil: {result}", fg="green")
        # Jika inputan user bukan angka, maka akan muncul error message 
        except Exception as e: # Exception akan diinisiasi dengan variabel "e".
            self.result_label.config(text=f"Input tidak valid: {e}", fg="red")

    # Method clear entries
    # Dijalankan ketika tombol "Clear" diklik.
    def clear_entries(self):
        # Menghapus/ mengkosongkan semua field input 
        for entry in self.entries.values():
            # Menghapus teks dari awal (0) sampai akhir (END).
            entry.delete(0, tk.END)
        # Mengkosongkan teks pada label hasil
        self.result_label.config(text="")
