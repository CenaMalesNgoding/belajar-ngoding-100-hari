teks = input("Masukkan teks: ")
simbol = any(not c.isalnum() and not c.isspace() for c in teks)
print("Mengandung simbol" if simbol else "Tidak ada simbol")
