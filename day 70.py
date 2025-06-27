angka = input("Masukkan angka: ")
total = sum(int(i) for i in angka if i.isdigit())
print("Jumlah digit:", total)
