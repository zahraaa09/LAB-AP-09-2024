usia = int(input("Masukkan usia: "))
keanggotaan = input("Apakah anda anggota (ya/tidak): ")

if usia < 5:
    harga = 0
elif usia >=5 and usia<= 12:
    harga = 50000
elif usia>= 13 and usia<= 59:
    harga = 100000
else:
    harga = 70000

harga = harga - (20/100)*(harga)
keanggotaan = harga if keanggotaan == "ya" else "tidak" 

print(f"Harga tiket: Rp. {int(harga)}")