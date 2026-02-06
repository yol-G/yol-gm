import tkinter as tk                      # mengimpor module tkinter
from tkinter import ttk                  # import ttk widget
from tkinter.messagebox import showinfo  # import showinfo

# ================= INIT =================
window = tk.Tk()                         # membuat object window
window.configure(bg="white")             # mengubah background window menjadi putih
window.geometry("300x200")               # mengubah size window (pixel)
window.resizable(False, False)           # window tidak bisa di-resize
window.title("Sapa")                     # judul window

# =============== VARIABLE ===============
NAMA_DEPAN = tk.StringVar()              # membuat constant
NAMA_BELAKANG = tk.StringVar()           # membuat constant

# =============== FUNGSI =================
def tombol_click():
    pesan = (
        "Hello "
        + NAMA_DEPAN.get()
        + " "
        + NAMA_BELAKANG.get()
        + ", Have nice day"
    )
    showinfo(title="Hi", message=pesan)

# ============== FRAME INPUT =============
input_frame = ttk.Frame(window)          # frame input
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# ============== KOMPONEN =================
# Label & Entry Nama Depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)

nama_depan_entry = ttk.Entry(
    input_frame,
    textvariable=NAMA_DEPAN
)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# Label & Entry Nama Belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

nama_belakang_entry = ttk.Entry(
    input_frame,
    textvariable=NAMA_BELAKANG
)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# Tombol
tombol = ttk.Button(
    input_frame,
    text="Sapa",
    command=tombol_click
)
tombol.pack(fill="x", expand=True, padx=10, pady=10)

# ============== MAINLOOP ================
window.mainloop()                        # menjalankan program
