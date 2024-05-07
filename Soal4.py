def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def rekomendasi_bmi(bmi):
    if bmi < 18.5:
        return "Berat Badan Kurang"
    elif bmi < 24.9:
        return "Berat Badan Normal"
    elif bmi < 29.9:
        return "Kelebihan Berat Badan"
    else:
        return "Obesitas"

berat_badan = float(input("Masukkan berat badan (kg) : "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))

bmi = hitung_bmi(berat_badan, tinggi_badan)
kategori_bmi = rekomendasi_bmi(bmi)


print(f"Berat Badan : {berat_badan} kg")
print(f"Tinggi Badan : {tinggi_badan} m")
print(f"Nilai BMI Anda : {bmi:.2f}")
print(f"Kategori BMI : {kategori_bmi}")