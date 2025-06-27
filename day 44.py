total = float(input("Total belanja: Rp "))
if total > 500000:
    diskon = total * 0.1
else:
    diskon = total * 0.05
print(f"Diskon: Rp {diskon}, Total bayar: Rp {total - diskon}")
