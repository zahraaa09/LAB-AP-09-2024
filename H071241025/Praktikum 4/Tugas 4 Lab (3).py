def hitung_langkah():
    n = input("Masukkan angka: ")

    try:
        n = int(n)
    except:
        print("Input tidak Valid")
        return

    langkah = 0
            
    while n != 1:
        if n % 2 == 0:  
            n = n / 2  
        else:  
            n = 3 * n + 1
        print(n)
        langkah += 1
            
    print(f"Jumlah langkah: {langkah}")

hitung_langkah()