import tkinter as tk # Mengimpor tkinter, modul GUI Python untuk membuat user interface
from ui.app_ui import DataScienceApp # Mengimpor kelas DataScienceApp dari modul app_ui yang ada di package ui, yang berisi aplikasi utama

if __name__ == "__main__":
    # Root adalah variabel yang digunakan sebagai referensi untuk primary window.
    root = tk.Tk() # Membuat window utama aplikasi menggunakan tkinter
    # DataScienceApp akan membangun UI di dalam root (primary window).
    app = DataScienceApp(root) # Membuat aplikasi DataScienceApp dan menghubungkannya dengan window root
    # Aplikasi akan terus berjalan dan merespon input user sampai window ditutup.
    root.mainloop()
