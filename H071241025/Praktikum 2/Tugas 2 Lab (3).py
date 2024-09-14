nilai = int(input("Masukkan nilai: "))
hadir = int(input("Masukkan persentase kehadiran: "))
ratarata = [70, 75, 80, 85, 90, 95, 100]

if hadir < 75:
    status = "Tidak Lulus"
else:
    if nilai >= 85 and nilai <= 100:
        status = "Lulus dengan Predikat A"
    elif nilai >= 70 and nilai <= 84:
        status = "Lulus dengan Predikat B"
    elif nilai >= 60 and nilai <= 69:
        status = "Lulus dengan Predikat C"
    elif nilai <= 60 and ratarata is True:
        status = "Lulus dengan predikat C"

print(status)