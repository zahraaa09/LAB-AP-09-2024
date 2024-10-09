def hitung_penghapusan_untuk_anagram(str1, str2):
    total_penghapusan = 0
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for char in alfabet:
        count1 = str1.count(char)
        count2 = str2.count(char)
        
        if count1 > count2:
            total_penghapusan += count1 - count2
        elif count2 > count1:
            total_penghapusan = total_penghapusan + (count2 - count1)
    
    return total_penghapusan

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

hasil = hitung_penghapusan_untuk_anagram(str1, str2)
print(f"Jumlah minimum penghapusan karakter untuk membuat anagram: {hasil}")