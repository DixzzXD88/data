print("Menu makanan :")
print("1.Nasgor goreng")
print("2.Kwetiau")

pilihan = input("Masukkan pilihan makanan : ")

match pilihan:
    case "1":
        print("Nasgor goreng")
        print("Harga Rp67.000")
    case "2":
        print("Kwetiau")
        print("Harga Rp676.000")
      
    case _:
        print("makanannya udah basi")


# ===== TUGAS 1 =====

print("===== MENU JURUSAN =====")
print("1. PPLG")
print("2. TJKT")
print("3. TKR")
print("4. TBSM")
print("5. AKL")

pilihan = input("Pilih jurusan : ")

match pilihan:
    case "1":
        print("Jurusan: PPLG")
        print("Bidang: Pengembangan Perangkat Lunak dan Gim")
    case "2":
        print("Jurusan: TJKT")
        print("Bidang: Teknik Jaringan Komputer dan Telekomunikasi")
    case "3":
        print("Jurusan: TKR")
        print("Bidang: Teknik Kendaraan Ringan")
    case "4":
        print("Jurusan: TBSM")
        print("Bidang: Teknik Bisnis Sepeda Motor")
    case "5":
        print("Jurusan: AKL")
        print("Bidang: Akuntansi dan Keuangan Lembaga")
    case _:
        print("Jurusan tidak tersedia")
        
