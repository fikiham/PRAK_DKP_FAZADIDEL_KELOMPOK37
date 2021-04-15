#method
import functions
from functions import Ac

la = functions.iden("37","2")
la.identitas()

li = functions.nama("Abdullah Faqih Mubarak","Didi Suhardi","Felisiana Ardelia Azzahra","Zakia Marrit")
li.anggota()

print("\n================ Pengaturan AC ================\n")

run = True
#perulangan while
while run:
    #variabel kondisi
    kondisi = input("Apakah kamu ingin menyalakan AC (Ya/Tidak)? ")
    
    #pengkondisian
    if kondisi == "Ya":
        print ("AC berhasil dinyalakan")
        suhu = input("\nMasukkan suhu yang anda inginkan = ")
        Ac.ubah(suhu)

        On = True
        while On:            
            kondisi = input("\nApakah anda ingin mengganti suhu (Ya/Tidak)? ")
            if kondisi == "Ya":
                suhu = input("Masukkan suhu yang anda inginkan = ")
                Ac.ubah(suhu)
            elif kondisi == "Tidak":
                print("Baik, Selamat menikmati ruangan anda\n")
                break
            else:
                print("Kondisi yang anda masukkan tidak tersedia, silahkan gunakan salah satu dari pilihan yang disediakan")
        break
    elif kondisi == "Tidak":
        print ("AC berhasil dimatikan. \nTerima Kasih telah memakai produk AC kami")
        break
    else:
        print("Kondisi yang anda masukkan tidak tersedia, silahkan gunakan salah satu dari pilihan yang disediakan")