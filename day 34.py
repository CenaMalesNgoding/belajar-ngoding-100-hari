# day34.py
def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b): return a / b if b != 0 else "Tidak bisa dibagi nol"

print("Operasi: 1. Tambah  2. Kurang  3. Kali  4. Bagi")
pilih = input("Pilih operasi (1/2/3/4): ")
a = float(input("Angka pertama: "))
b = float(input("Angka kedua: "))

if pilih == "1":
    print("Hasil:", tambah(a, b))
elif pilih == "2":
    print("Hasil:", kurang(a, b))
elif pilih == "3":
    print("Hasil:", kali(a, b))
elif pilih == "4":
    print("Hasil:", bagi(a, b))
else:
    print("Pilihan tidak valid")
