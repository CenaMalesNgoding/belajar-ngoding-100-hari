teks = input("Masukkan kalimat: ")
print("Mengandung angka" if any(c.isdigit() for c in teks) else "Tidak mengandung angka")
