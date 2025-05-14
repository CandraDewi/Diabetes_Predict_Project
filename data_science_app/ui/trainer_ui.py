import tkinter as tk
from tkinter import filedialog, messagebox
from model.trainer import train_and_save_model
import subprocess
import os

#kelas utama untuk membuat tampilan trainer model
class TrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Training Model Diabetes")
        self.root.geometry("500x200")

        self.label = tk.Label(root, text="Upload dataset training:")
        self.label.pack(pady=10)

        self.upload_btn = tk.Button(root, text="Upload Dataset", command=self.load_dataset)
        self.upload_btn.pack(pady=5)


    #fungsi yang digunakan untuk membaca dataset yang akan di training
    def load_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        try:
            train_and_save_model(file_path)
            messagebox.showinfo("Sukses", "Model berhasil dilatih dan disimpan.")

            self.root.destroy()
            main_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "main.py"))
            subprocess.Popen(["python", main_path])

        except Exception as e:
            messagebox.showerror("Error", f"Gagal melakukan training: {e}")

#Fungsi pembuka GUI training model (dipanggil dari main)
def run_trainer_ui():
    root = tk.Tk()
    app = TrainerApp(root)
    root.mainloop()

#Jika file dijalankan secara langsung, GUI akan dijalankan
if __name__ == "__main__":
    run_trainer_ui()
