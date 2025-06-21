from datetime import datetime

tahun_lahir = int(input("Masukkan tahun lahir kamu: "))
tahun_sekarang = datetime.now().year
umur = tahun_sekarang - tahun_lahir
print(f"Umur kamu sekarang adalah {umur} tahun.")
