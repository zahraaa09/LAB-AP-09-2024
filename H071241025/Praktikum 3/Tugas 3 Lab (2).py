import random

angka_rahasia = random.randint(1,100)
percobaan = 0
max = 5

while percobaan < max:
    try:
        tebak = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))

        if tebak == 0:
            print("Permainan dihentikan.")
            break
        percobaan += 1

        if tebak > angka_rahasia:
            print("Angka terlalu besar.")
        elif tebak < angka_rahasia:
            print("Angka terlalu kecil.")
        else:
            print("Selamat! Anda menebak angka dengan benar.")
            break

        if percobaan == max:
            print("Anda telah kehabisan percobaan. Silahkan coba lagi.")

    except:
        print("Inputan harus berisi angka.")
