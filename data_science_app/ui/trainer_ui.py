import tkinter as tk # Modul GUI Python untuk membuat user interface
from tkinter import filedialog, messagebox # Komponen tambahan untuk memilih file (filedialog) dan menampilkan pesan pop-up info atau error
from model.trainer import train_and_save_model # Mengimpor fungsi pelatihan model dari modul trainer yang telah dibuat
import subprocess # Mengimport subprocess untuk menjalankan kembali main.py setelah training selesai
import os # Mengimport os untuk menjalankan kembali main.py setelah training selesai

# Kelas utama untuk membuat tampilan pelatihan model (trainer GUI)
class TrainerApp:
    def __init__(self, root):
        self.root = root # Menyimpan root window ke atribut kelas
        self.root.title("Training Model Diabetes") # Judul jendela utama
        self.root.geometry("500x200") # Ukuran jendela

        # Label instruksi untuk upload dataset
        self.label = tk.Label(root, text="Upload dataset training:")
        self.label.pack(pady=10) # Memberikan jarak vertikal 5 piksel

        self.upload_btn = tk.Button(root, text="Upload Dataset", command=self.load_dataset)
        self.upload_btn.pack(pady=5)

    # Fungsi yang dijalankan saat tombol "Upload Dataset" ditekan
    def load_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")]) # Membuka file dialog dan meminta user untuk memilih file CSV
        if not file_path:  # Jika user membatalkan pemilihan file, fungsi tidak dilanjutkan
            return

        try:
            train_and_save_model(file_path)  # Memanggil fungsi training dan menyimpan model ke file
            messagebox.showinfo("Sukses", "Model berhasil dilatih dan disimpan.") # Jika sukses, akan menampilkan pop-up informasi

            self.root.destroy()  # Menutup jendela pelatihan karena proses sudah selesai
            main_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "main.py")) # Mencari path ke main.py supaya bisa dijalankan ulang setelah training
            subprocess.Popen(["python", main_path]) # Menjalankan kembali program utama (main.py) sebagai proses terpisah

        except Exception as e: # Jika terdapat error selama proses training, akan menampilkan pesan error ke user
            messagebox.showerror("Error", f"Gagal melakukan training: {e}") 

# Fungsi pembuka GUI training model (dipanggil dari main)
def run_trainer_ui():
    root = tk.Tk() # Membuat jendela root utama
    app = TrainerApp(root) #  Menginisialisasi aplikasi TrainerApp
    root.mainloop() # Menjalankan loop utama GUI

# Jika file dijalankan secara langsung, GUI akan dijalankan
if __name__ == "__main__":
    run_trainer_ui()
