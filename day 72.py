teks = input("Masukkan teks: ")
unik = ""
for huruf in teks:
    if huruf not in unik:
        unik += huruf
print("Karakter unik:", unik)
