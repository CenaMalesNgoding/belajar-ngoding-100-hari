teks = input("Teks: ")
kar = input("Karakter: ")
tengah = len(teks) // 2
hasil = teks[:tengah] + kar + teks[tengah:]
print("Hasil:", hasil)
