import tkinter as tk
from tkinter import ttk, messagebox

BIAYA_PER_JAM = 2000

def hitung_biaya():
    try:
        plat = entry_plat.get()
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())

        if keluar < masuk:
            messagebox.showerror("Error", "Waktu keluar tidak valid")
            return

        lama = keluar - masuk
        biaya = lama * BIAYA_PER_JAM

        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, f"{biaya}")

        # Masuk ke tabel pelanggan
        tree.insert("", "end", values=(plat, masuk, keluar, biaya))

    except ValueError:
        messagebox.showerror("Error", "Input harus angka")

# Window utama
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("800x450")

# ===== Judul =====
judul = tk.Label(root, text="Aplikasi Parkir Kelompok 6",
                 font=("Arial", 14, "bold"))
judul.pack(pady=10)

# ===== Frame Atas =====
frame_atas = tk.Frame(root)
frame_atas.pack(fill="x", padx=20)

# ===== Frame Input =====
frame_input = tk.LabelFrame(frame_atas, text="Cari Plat")
frame_input.pack(side="left", padx=10)

tk.Label(frame_input, text="No Plat Polisi").grid(row=0, column=0, sticky="w")
entry_plat = tk.Entry(frame_input, width=20)
entry_plat.grid(row=0, column=1, pady=2)

tk.Label(frame_input, text="Waktu Masuk").grid(row=1, column=0, sticky="w")
entry_masuk = tk.Entry(frame_input)
entry_masuk.grid(row=1, column=1, pady=2)

tk.Label(frame_input, text="Waktu Keluar").grid(row=2, column=0, sticky="w")
entry_keluar = tk.Entry(frame_input)
entry_keluar.grid(row=2, column=1, pady=2)

tk.Label(frame_input, text="Biaya").grid(row=3, column=0, sticky="w")
entry_biaya = tk.Entry(frame_input)
entry_biaya.grid(row=3, column=1, pady=2)

tk.Button(frame_input, text="Submit", command=hitung_biaya)\
    .grid(row=4, columnspan=2, pady=5)

# ===== Frame Biaya =====
frame_biaya = tk.Frame(frame_atas)
frame_biaya.pack(side="right", padx=30)

tk.Label(frame_biaya, text="Biaya Per Jam",
         font=("Arial", 12, "bold")).pack()
tk.Label(frame_biaya, text="Rp. 2.000",
         font=("Arial", 20, "bold"), fg="red").pack()

# ===== Tabel Pelanggan =====
frame_tabel = tk.LabelFrame(root, text="List Pelanggan Untuk Terakhir Keluar")
frame_tabel.pack(fill="both", expand=True, padx=20, pady=20)

columns = ("No Plat Polisi", "Masuk", "Keluar", "Biaya")
tree = ttk.Treeview(frame_tabel, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True)

root.mainloop()
