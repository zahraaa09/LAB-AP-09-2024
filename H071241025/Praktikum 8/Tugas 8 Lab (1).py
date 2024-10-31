import re

def validasi_string():
    while True:
        inputan = input("Masukkan string (45 karakter): ")
        pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'

        if len(inputan) != 45:
            print("False")
        else:
            hasil = re.match(pattern, inputan)
            if hasil:
                print("True")
                break
            else:
                print("False")

validasi_string()