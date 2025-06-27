def is_prima(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

angka = int(input("Masukkan angka: "))
print("Prima" if is_prima(angka) else "Bukan prima")
