print("Mencari karakter dalam kalimat.")

karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")

pesan = (f'Karakter merupakan bagian dari Kalimat "{kalimat}"' * (karakter in kalimat)) or (f'Karakter tidak ditemukan dalam Kalimat "{kalimat}"' * (karakter not in kalimat))

print(pesan)
