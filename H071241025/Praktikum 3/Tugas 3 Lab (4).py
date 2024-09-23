pecahan =[100000, 50000, 20000, 10000, 5000, 2000, 1000]

try:
    harga = int(input("Masukkan total harga: "))
    uang = int(input("Masukkan uang yang diberikan: "))
    kembalian = uang - harga

    for i in pecahan:
        lembar_kembalian = kembalian // i
        if lembar_kembalian > 0:
            print(f"{lembar_kembalian} lembar Rp {i}")
            kembalian -= lembar_kembalian * i

except ValueError:
    print("Mohon masukkan angka yang valid.")

