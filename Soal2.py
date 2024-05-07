def tahunkabisat(tahun):
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
tahun = int(input("Masukkan tahun: "))

if tahunkabisat(tahun):
    print(f"Tahun {tahun} merupakan TAHUN KABISAT")
else:
    print(f"Tahun {tahun} bukanlah TAHUN KABISAT")
    
