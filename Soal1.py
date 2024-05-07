bilangan_pertama = int(input("Masukkan bilangan pertama: "))
bilangan_kedua = int(input("Masukkan bilangan kedua: "))

hasil_penjumlahan = bilangan_pertama + bilangan_kedua
hasil_pengurangan = bilangan_pertama - bilangan_kedua
hasil_modulus = bilangan_pertama % bilangan_kedua

print('''
Hasil Perhitungan: 
      ''')
print(f"Penjumlahan: {hasil_penjumlahan}")
print(f"Pengurangan: {hasil_pengurangan}")
print(f"Modulus: {hasil_modulus}")