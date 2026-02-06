# Fungsi untuk menghitung rata-rata dari sejumlah angka
def hitung_rata_rata(angka):
total = sum(angka)
rata_rata = total / len(angka)
return rata_rata

#Fungsi untuk mendapatkan input angka dari pengguna
def input_angka():
    angka = []
    while True:
        try:
            bilangan = float(input("masukkan angka (0 untuk mengakhiri):"))
            if bilangan == 0:
                break 
            angka.append(bilangan)
        except ValueError:
            print("Masukkan angka yang valid.")
    return angka 

#program utama 
if _name_=="_main_":
    print("program Menghitung Rata-Rata")
    daftar_angka = input_angka()

    if daftar angka:
        rata_rata = hitung rata_rata(daftar_angka)
        print(f"Rata-rata dari angka-angka yang dimasukkan adalah:(rata_rata:.2f)")
    else:
        print("tidak ada angka yang dimasukkan.")    