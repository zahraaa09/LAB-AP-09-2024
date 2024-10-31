import random # untuk membuat nomor random pada nama tiket
import datetime # waktu dalam pemesanan filmnha
import os # untuk membuat folder film dan tiketnya

def menu_awal():
    print("\n---Sistem Pemesanan Tiket Bioskop---")
    print("1. Admin")
    print("2. Pengunjung")
    print("3. Keluar")

def menu_admin():
    print("\n---Menu Admin---")
    print("1. Tambah Film")
    print("2. Hapus Film")
    print("3. Daftar Tiket")
    print("4. Kembali")

daftar_film = []

def tambah_film():
    while True: # agar menu tambah film terus berulang 
        print("\n---Tambah Film---")
        tambah = input("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
        if tambah != "":
            print(f"Film '{tambah}' berhasil ditambahkan.")
            daftar_film.append(f"{tambah}")
            os.makedirs('film', exist_ok=True) # membuat foldernya
            with open(f"film/{tambah}.txt", "w") as file: # membuat file nama film di dalam folder film nya
                file.write(f"Film: {tambah}\n")
        else:
            print("\nKembali ke Menu Admin")
            break

def hapus_film():
    while True:
        print("\n---Hapus Film---")
        for i, film in enumerate(daftar_film, start=1): # untuk membuat film yang ada itu berurut, dimulai dari 1
            print(f"Daftar film: \n{i}. {film}")
        print("0. Kembali")
        hapus = int(input("Masukkan nomor file yang ingin dihapus (atau 0 untuk kembali): "))
        if hapus > 0 and hapus <= len(daftar_film):
            index = hapus - 1
            dihapus = daftar_film.pop(index) # menghapus film dari list
            print(f"Film '{dihapus}' berhasil dihapus")    
        elif hapus == "0":
            print("\nKembali ke Menu Admin.")
            break
        elif hapus != int:
            print("Input tidak valid.")
        else:
            print("Nomor film tidak valid.")
        break

def menu_pengunjung():
    print("\n---Menu Pengunjung---")
    print("1. Lihat daftar film")
    print("2. Beli tiket")
    print("3. Kembali")

def lihat_Daftarfilm():
    if not daftar_film: # jika daftar film masih kosong
        print("Daftar film kosong.")
    else:
        print("---Daftar Film---")
        for i, film in enumerate(daftar_film, start=1):
            print(f"{i}. {film}")

id_tiket = []

def beli_tiket():
    if not daftar_film:
        print("Tidak ada film yang tersedia untuk dibeli.")
        return
    for i, film in enumerate(daftar_film, start=1):
        print(f"\nDaftar film: \n{i}. {film}")
        print("0. Kembali")
    beli = input("Pilih nomor film yang ingin ditonton: (atau 0 untuk kembali): ")
    if beli == "0":
        return # kembali ke menu pengunjung
    try:
        nomor_film = int(beli)
        if 1 <= nomor_film <= len(daftar_film):
            pilih_film = daftar_film[nomor_film - 1]
            ID = f"TICK{random.randint(1000000000,9999999999)}"
            id_tiket.append(f"{ID}")
            waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            lebar_tiket = 40

            os.makedirs('tickets', exist_ok=True) # membuat folder tiket

            with open(f"tickets/{ID}.txt", "a") as file: # membuat file tiket
                file.write("+" + "-" * lebar_tiket + "+\n")                
                file.write("|" + " " + "TIKET BIOSKOP".center(lebar_tiket - 2) + " " + "|\n")
                file.write("+" + "-" * lebar_tiket + "+\n")
                file.write("|" + " ID Tiket: " + ID + " " * (lebar_tiket - len(ID) - 9) + "|\n")
                file.write("|" + " Film: " + pilih_film + " " * (lebar_tiket - len(pilih_film) - 5) + "|\n")
                file.write("|" + " Tanggal: " + waktu + " " * (lebar_tiket - len(waktu) - 10) + "|\n")
                file.write("+" + "-" * lebar_tiket + "+\n")                
                file.write("|" + " " + "Terima Kasih telah membeli tiket Anda!".center(lebar_tiket - 2) + "|\n")
                file.write("+" + "-" * lebar_tiket + "+\n")

            print(f"\nTiket berhasil dibeli. ID Tiket Anda: {ID}")
            print(f"\nFile tiket telah dibuat: tickets/{ID}.txt")
        else:
            print("\nNomor film tidak valid.")
    except ValueError:
        print("\nInput tidak valid.")

def daftar_tiket():
    while True:
        print("\n--- Daftar Tiket---")
        print("1. Lihat Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("4. Kembali")
        opsi = input("Pilih opsi (1/2/3/4): ")
        if opsi == "1":
            lihat_Daftartiket()
        elif opsi == "2":
            lihat_Detailtiket()
        elif opsi == "3":
            hapus_tiket()
        elif opsi == "4":
            print("\nKembali ke Menu Admin.")
            break
        else:
            print("Mohon input angka 1/2/3/4.")

def lihat_Daftartiket():
    if not id_tiket:
        print("Daftar tiket kosong.")
    else:
        for i, tiket in enumerate(id_tiket, start=1):
            print(f"Daftar tiket: \n{i}. {tiket}")

def lihat_Detailtiket():
    lihat_Daftartiket()
    print("0. Kembali")
    pilih = input("Pilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): ")
    if pilih == "0":
        daftar_tiket()
    else:
        try:
            nomor_tiket = int(pilih)
            if nomor_tiket >= 1 and nomor_tiket <= len(id_tiket):
                tiket_id = id_tiket[nomor_tiket - 1]
                with open(f"tickets/{tiket_id}.txt", "r") as file:
                        print("\n----Detail Tiket---")
                        print(file.read())
            else:
                print("Nomor tiket tidak valid.")
        except ValueError:
            print("Input tidak valid.")

def hapus_tiket():
    lihat_Daftartiket()
    print("0. Kembali")
    nomor = input("Pilih nomor tiket yang ingin dihapus (atau 0 untuk  kembali): ")
    if nomor == "0":
        print("\nKembali ke Daftar Tiket.")
        daftar_tiket()
    else:
        try:
            nomor_tiket = int(nomor)
            if nomor_tiket >= 1 and nomor_tiket <= len(id_tiket):
                tiket_id = id_tiket[nomor_tiket - 1]
                os.remove(f"tickets/{tiket_id}.txt")
                id_tiket.pop(nomor_tiket - 1)
                print(f"Tiket dengan ID {tiket_id} telah dihapus.")
            else:
                print("Nomor tiket tidak valid.")
        except ValueError:
            print("Input tidak valid.")

def main():
    while True:
        menu_awal()
        peran = input("Pilih peran (1/2/3): ")
        if peran == "1":
            while True:
                menu_admin()
                opsi = input("Pilih Opsi (1/2/3/4): ")
                if opsi == "4":
                    print("\nKembali ke Menu Utama.")
                    break
                elif opsi == "1":
                    tambah_film()
                elif opsi == "2":
                    hapus_film()
                elif opsi == "3":
                    daftar_tiket()
                else: 
                    print("Mohon masukka angka 1/2/3/4")
        elif peran == "2":
            while True:
                menu_pengunjung()
                opsi = input("Pilih opsi (1/2/3): ")
                if opsi == "1":
                    lihat_Daftarfilm()
                elif opsi == "2":
                    beli_tiket()
                elif opsi == "3":
                    print("\nKembali ke Menu Utama.")
                    break
            
        elif peran == "3":
            print("Terima Kasih telah menggunakan sistem ini.")
            break
        else:
            print("Mohon masukkan angka 1, 2 atau 3.")

main()