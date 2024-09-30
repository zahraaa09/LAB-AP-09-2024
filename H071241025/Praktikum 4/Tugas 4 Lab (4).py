def kalkulator_sederhana():
    print("Selamat datang di Kalkulator Sederhana!")
    
    while True:
    
        try:
            angka1 = float(input("Angka pertama: "))
        except ValueError as a:
            print(f"Input tidak valid:'{a}'")
            break
        try:
            angka2 = float(input("Angka kedua: "))
        except ValueError as a:
            print(f"Input tidak valid: '{a}'")
            break
            
        operasi = input("Operasi (+, -, *, /): ")
        list_operasi = [ "+", "-", "/", "*" ]
        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        elif operasi == "/":
            if angka2 != 0:
                hasil = angka1 / angka2
            else:
                print("Pembagian dengan nol tidak diperbolehkan.")
            break
        elif operasi not in list_operasi:
            print("Operasi tidak valid. Gunakan +, -, *, atau /.")
            break
            
        print(f"Hasil: {hasil}")
        break

kalkulator_sederhana()