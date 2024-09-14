sisi1 = input("Masukkan panjang sisi pertama: ") 
sisi2 = input("Masukkan panjang sisi kedua: ")
sisi3 = input("Masukkan panjang sisi ketiga: ")

if sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0:
    print("Segitiga tidak valid.")
elif sisi1 + sisi2 <= sisi3 or sisi1 + sisi3 <= sisi2 or sisi2 + sisi3 <= sisi1:
    print("Segitiga tidak valid.")
else:
    if sisi1 == sisi2 == sisi3:
        print("Segitiga sama Sisi.")
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        print("Segitiga sama Kaki.")
    else:
        print("Tidak dapat membentuk segitiga yang valid.") # Termasuk segitiga sembarang