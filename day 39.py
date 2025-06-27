import random, string

panjang = int(input("Panjang password: "))
karakter = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(karakter) for _ in range(panjang))
print("Password:", password)
