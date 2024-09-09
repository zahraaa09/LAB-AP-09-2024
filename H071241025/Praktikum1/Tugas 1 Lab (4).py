print("Konversi suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit.")

celcius = int(input("Masukkan suhu dalam satuan Celvius:"))
kelvin = celcius + 273
reamur = celcius * (4/5)
fahrenheit = (celcius * (9/5)) + 32

print(f"Hasil dari konversi suhu Kelvin adalah: {kelvin}K")
print(f"Hasil dari konversi suhu Reamur adalah: {reamur}R")
print(f"Hasil dari konversi suhu Fahrenheit adalah: {fahrenheit}F")