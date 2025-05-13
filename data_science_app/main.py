import tkinter as tk # Untuk membuat GUI
from ui.app_ui import DataScienceApp # mengimpor kelas DataScienceApp dari modul app_ui yang ada di package ui.

if __name__ == "__main__":
    # Root adalah variabel yang digunakan sebagai referensi untuk primary window.
    root = tk.Tk() # Membuat window utama aplikasi
    # DataScienceApp akan membangun UI di dalam root (primary window).
    app = DataScienceApp(root)
    # Aplikasi akan terus berjalan dan merespon input user sampai window ditutup.
    root.mainloop()
