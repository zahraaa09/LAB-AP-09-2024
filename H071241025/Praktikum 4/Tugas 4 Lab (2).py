# def harta_karun():
#     total_jarak=0

#     while True:
#         jarak_langkah = input("Masukkan langkah (meter) atau 0 untuk selesai: ")
#         try:
#             jarak_langkah = int(jarak_langkah)
#         except:
#             print("Input tidak valid. Masukkan bilangan bulat.")
#             continue
        
#         total_jarak = total_jarak + jarak_langkah

#         def keputusan():
#             print(f"Total jarak: {total_jarak} meter")
#             if total_jarak > 20:
#                 bahaya = "Ya"
#                 keputusan_akhir = "Tidak aman menggali harta karun. Coba lagi!"
#             elif total_jarak == 50:
#                 bahaya = "Tidak"
#                 keputusan_akhir = "Aman, selamat anda mendapatkan harta karun"
#             else:
#                 bahaya = "Tidak"
#                 keputusan_akhir = "Aman! Kamu tepat menemukan harta karun dan menang!"
#             print(f"Ada bahaya: {bahaya}")
#             print(f"Keputusan: {keputusan_akhir}")
            
#         if jarak_langkah == 0:
#             keputusan()
#             break

# harta_karun()

def pemburu_harta_karun():
    total_distance = 0
    while True:
        try:
            langkah = int(input('Masukkan langkah (meter) atau 0 untuk selesai: '))
            if langkah < 0 :
                print('Input tidak valid. Permainan berhenti.')
                break
            if langkah > 20:
                print('Ada bahaya: Ya')
            total_distance = total_distance + langkah
            if langkah != 0:
                continue
            print(f'Total jarak: {total_distance} meter')
            if total_distance > 50:
                print('Ada bahaya: Ya')
                print('Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!')
            elif total_distance < 50:
                print('Ada bahaya: Tidak')
                print('Keputusan: Tidak menemukan harta karun. Coba lagi!')
            else:
                print('Ada bahaya: Tidak')
                print('Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!')
            break
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

pemburu_harta_karun()