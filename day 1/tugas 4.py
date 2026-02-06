# Program menentukan kategori umur berdasarkan flowchart

# Input
umur = int(input("Masukkan umur: "))

# Proses & Output
if umur <= 10:
    print("Kategori: Anak-anak")
elif umur <= 18:
    print("Kategori: Remaja")
elif umur <= 35:
    print("Kategori: Dewasa")
elif umur <= 65:
    print("Kategori: Parubaya")
else:
    print("Kategori: Tua")
