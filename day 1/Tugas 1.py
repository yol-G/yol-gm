print("PROGRAM POLA BINTANG")

# input jumlah baris
n = int(input("Masukkan jumlah baris: "))

# segitiga sama kaki
print("\nSegitiga Bintang Sama Kaki")
for i in range(1, n + 1):
    spasi = n - i
    bintang = i

    print(" " * spasi, end="")
    for j in range(bintang):
        print("*", end=" ")
    print()

# segitiga siku-siku
print("\nSegitiga Bintang Siku-Siku")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
