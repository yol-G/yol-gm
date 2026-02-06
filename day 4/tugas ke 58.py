import tkinter as tk
from tkinter import ttk

# ============== FUNGSI UNTUK MENGHITUNG ==============
def hitung():
    angka1 = float(angka1_entry.get())
    angka2 = float(angka2_entry.get())
    operator = operator_combo.get()

    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        hasil = angka1 / angka2
    else:
        hasil = "Operator tidak valid"

    hasil_label.config(text=f"Hasil: {hasil}")

# ================== MEMBUAT JENDELA ==================
window = tk.Tk()
window.title("Kalkulator")

# =================== FRAME INPUT =====================
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

# ================== ANGKA 1 ==========================
angka1_label = ttk.Label(input_frame, text="Angka 1")
angka1_label.grid(row=0, column=0, sticky="w")

angka1_entry = ttk.Entry(input_frame)
angka1_entry.grid(row=1, column=0)

# ================== ANGKA 2 ==========================
angka2_label = ttk.Label(input_frame, text="Angka 2")
angka2_label.grid(row=0, column=1, sticky="w")

angka2_entry = ttk.Entry(input_frame)
angka2_entry.grid(row=1, column=1)

# ================== OPERATOR =========================
operator_label = ttk.Label(input_frame, text="Operator")
operator_label.grid(row=2, column=0, sticky="w")

operator_combo = ttk.Combobox(
    input_frame,
    values=["+", "-", "*", "/"]
)
operator_combo.grid(row=3, column=0)
operator_combo.current(0)

# ================== TOMBOL HITUNG ====================
hitung_button = ttk.Button(
    window,
    text="Hitung",
    command=hitung
)
hitung_button.pack(pady=10)

# ================== LABEL HASIL ======================
hasil_label = ttk.Label(window, text="Hasil:")
hasil_label.pack()

# ================== MAINLOOP =========================
window.mainloop()
