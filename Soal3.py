
jumlah_barang = int(input("Masukkan jumlah barang: "))
total_biaya = 0

for i in range(1, jumlah_barang + 1):
    harga_barang = float(input(f"Masukkan harga barang ke-{i}: "))
    total_biaya += harga_barang

print("\nHasil Perhitungan Total Biaya:")
print(f"Jumlah Barang: {jumlah_barang}")
print(f"Harga Barang ke-1: {harga_barang}")
print(f"Harga Barang ke-2: {harga_barang}")
print(f"Total Biaya: {total_biaya}")