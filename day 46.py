import random
angka = random.randint(1, 10)
tebak = int(input("Tebak angka 1-10: "))
if tebak == angka:
    print("Tebakan benar!")
else:
    print(f"Salah. Angka yang benar: {angka}")
