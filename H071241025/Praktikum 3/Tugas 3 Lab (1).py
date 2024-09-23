baris = int(input("Masukkan jumlah baris: "))

for i in range(baris+1):
    if i % 2 != 1:
        continue
    a = " * "*i
    hasil = a.center(baris*3, " ")
    print(hasil)
    
for i in range (baris-1, -1, -1):
    if i % 2 == 0:
        continue
    a = " * "*i
    hasil = a.center(baris*3, " ")
    print(hasil)
