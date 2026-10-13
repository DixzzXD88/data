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
        
# ===== TUGAS 2 =====

print("===== KALKULATOR =====")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

operasi = input("Pilih operasi : ")
b1 = int(input("Masukkan bilangan 1 : "))
b2 = int(input("Masukkan bilangan 2 : "))

penjumlahan = b1 + b2
pengurangan = b1 - b2
perkalian = b1 * b2
pembagian = b1 / b2

match operasi:
     case "1":
         print(f"Hasilnya adalah = {penjumlahan}")
     case "2":
         print(f"Hasilnya adalah = {pengurangan}")
     case "3":
         print(f"Hasilnya adalah = {perkalian}")
     case "4":
         print(f"Hasilnya adalah = {pembagian}")
     case _:
         print("Pilihan operasi tidak ditemukan")
