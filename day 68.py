data = input("Masukkan sesuatu: ")
try:
    val = eval(data)
    print("Tipe:", type(val))
except:
    print("Tipe: str")
