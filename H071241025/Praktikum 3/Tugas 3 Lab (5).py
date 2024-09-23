populasi1 = int(input("Masukkan populasi awal serangga A: "))
populasi2 = int(input("Masukkan populasi awal serangga B: "))
hari = int(input("Masukkan jumlah hari: "))

for i in range(1, hari + 1):
    if i % 2 != 0:
        populasi1 *= 1.3 # karena penambahan 30%
        populasi2 *= 1.5 # karena penambahan 50%
    else:
        populasi1 *= 0.8 # karena penurunan 20%
        populasi2 *= 0.6 # karena penurunan 40%

    if i % 5 == 0:
        populasi1 *= 0.9 # predator memakan 10%
        populasi2 *= 0.9 
        print(f"Hari {i}: Predator memakan 10% populasi.")

    print(f"Hari {i}: Serangga A = {int(populasi1)}, Serangga B = {int(populasi2)}")