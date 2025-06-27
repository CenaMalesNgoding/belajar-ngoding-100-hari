from datetime import date
tahun = int(input("Tahun lahir: "))
bulan = int(input("Bulan lahir: "))
hari = int(input("Hari lahir: "))
lahir = date(tahun, bulan, hari)
sekarang = date.today()
umur = sekarang.year - lahir.year - ((sekarang.month, sekarang.day) < (lahir.month, lahir.day))
print("Umur kamu:", umur, "tahun")
