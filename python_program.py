import math

def kombinasi(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def segitiga_pascal(rows):
    for i in range(rows):
        print(" " * (rows - i), end="")  
        for j in range(i + 1):
            print(kombinasi(i, j), end=" ")
        print()  

def ganjil_genap_awal_akhir(awal, akhir):
    ganjil_count = 0
    genap_count = 0
    
    for i in range(awal, akhir + 1):
        if i % 2 == 0:
            genap_count += 1
        else:
            ganjil_count += 1

    print(f"Jumlah angka genap di rentang {awal} hingga {akhir}: {genap_count}")
    print(f"Jumlah angka ganjil di rentang {awal} hingga {akhir}: {ganjil_count}")

def menu_utama():
    while True:
        print("\nMenu Utama:")
        print("1. Segitiga Pascal")
        print("2. Ganjil Genap")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            #Segitiga Pascal
            while True:
                rows = int(input("Masukkan jumlah baris segitiga Pascal: "))
                segitiga_pascal(rows)
                
                ulang = input("Ingin mencoba lagi (y/n)? ").lower()
                if ulang == 'n':
                    break
                elif ulang != 'y':
                    print("Input tidak valid, kembali ke menu utama.")
                    break

        elif pilihan == "2":
            # ganjil genap
            while True:
                awal = int(input("Masukkan nilai awal rentang: "))
                akhir = int(input("Masukkan nilai akhir rentang: "))
                ganjil_genap_awal_akhir(awal, akhir)
                
                ulang = input("Ingin mencoba lagi (y/n)? ").lower()
                if ulang == 'n':
                    break
                elif ulang != 'y':
                    print("Input tidak valid, kembali ke menu utama.")
                    break

        elif pilihan == "3":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

menu_utama()
