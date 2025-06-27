def faktorial(n):
    return 1 if n == 0 else n * faktorial(n-1)

n = int(input("Masukkan angka: "))
print(f"Faktorial dari {n} adalah {faktorial(n)}")
