def buat_akronim(teks):
    kata_kata = teks.split()
    akronim = ''.join(kata[0].upper() for kata in kata_kata)
    return akronim

teks_input = input("Masukkan teks: ")
akronim_output = buat_akronim(teks_input)
print(akronim_output)