teks = input("Masukkan teks: ").lower()
vokal = "aiueo"
jumlah = sum(1 for huruf in teks if huruf in vokal)
print("Jumlah vokal:", jumlah)
