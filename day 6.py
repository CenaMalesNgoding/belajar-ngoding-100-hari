a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
operator = input("Pilih operasi (+, -, *, /): ")

if operator == "+":
    print("Hasil:", a + b)
elif operator == "-":
    print("Hasil:", a - b)
elif operator == "*":
    print("Hasil:", a * b)
elif operator == "/":
    if b != 0:
        print("Hasil:", a / b)
    else:
        print("Tidak bisa dibagi nol.")
else:
    print("Operasi tidak valid.")
