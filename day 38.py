teks = input("Masukkan kata/kalimat: ").replace(" ", "").lower()
if teks == teks[::-1]:
    print("Palindrome")
else:
    print("Bukan palindrome")
