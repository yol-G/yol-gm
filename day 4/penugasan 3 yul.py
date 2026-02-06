import tkinter as tk
from tkinter import messagebox

def simpan_data():
    data = {
        "Nama": entry_nama.get(),
        "Status": entry_status.get(),
        "Tanggal Lahir": entry_ttl.get(),
        "Asal Sekolah": entry_sekolah.get(),
        "NISN": entry_nisn.get(),
        "Nama Ayah": entry_ayah.get(),
        "Nama Ibu": entry_ibu.get(),
        "Telepon": entry_telp.get(),
        "Alamat": text_alamat.get("1.0", tk.END)
    }

    messagebox.showinfo("Simpan", "Data berhasil disimpan!")

def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_status.delete(0, tk.END)
    entry_ttl.delete(0, tk.END)
    entry_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_telp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# Window utama
root = tk.Tk()
root.title("MainWindow")
root.geometry("500x600")
root.configure(bg="#e6e6e6")

# ===== Judul =====
judul = tk.Label(
    root,
    text="DATA SISWA BARU",
    font=("Arial", 16, "bold"),
    bg="#8fd3d3"
)
judul.pack(fill="x", pady=10)

# ===== Frame Form =====
frame = tk.Frame(root, bg="#e6e6e6")
frame.pack(padx=20, pady=10, fill="x")

def buat_label_entry(text, row):
    tk.Label(frame, text=text, bg="#e6e6e6").grid(row=row, column=0, sticky="w")
    entry = tk.Entry(frame, width=40)
    entry.grid(row=row, column=1, pady=5)
    return entry

entry_nama = buat_label_entry("Nama Lengkap", 0)
entry_status = buat_label_entry("Siswa Baru", 1)
entry_ttl = buat_label_entry("Tanggal Lahir", 2)
entry_sekolah = buat_label_entry("Asal Sekolah", 3)
entry_nisn = buat_label_entry("NISN", 4)
entry_ayah = buat_label_entry("Nama Ayah", 5)
entry_ibu = buat_label_entry("Nama Ibu", 6)
entry_telp = buat_label_entry("Nomor Telepon / HP", 7)

# Alamat
tk.Label(frame, text="Alamat", bg="#e6e6e6").grid(row=8, column=0, sticky="nw")
text_alamat = tk.Text(frame, width=30, height=4)
text_alamat.grid(row=8, column=1, pady=5)

# ===== Frame Tombol =====
frame_btn = tk.Frame(root, bg="#8fd3d3")
frame_btn.pack(fill="x", side="bottom")

btn_hapus = tk.Button(frame_btn, text="Hapus", bg="#d36b5c", fg="white",
                      width=10, command=hapus_data)
btn_hapus.pack(side="right", padx=10, pady=10)

btn_simpan = tk.Button(frame_btn, text="Simpan", bg="#4caf50", fg="white",
                       width=10, command=simpan_data)
btn_simpan.pack(side="right")

root.mainloop()
