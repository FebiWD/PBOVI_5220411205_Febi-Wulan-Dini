#ulang
import os
os.system ('cls')


nama =str(input("Masukkan Nama anda :"))
noHp=int(input("masukkan no.hp : "))

def daftarMatkul():
        print("")
        print("=====================================================================")
        print("                         Kos Putri Velen                      ")
        print("")
        print("     1. Kategori Premium ==> 3X Cicilin dalam 1 tahun")
        print("     2. Kategori Exclusive ==> 4X Cicilin dalam 1 tahun")
        print("     3. Kategori Reguler ==> 6X Cicilin dalam 1 tahun")
        print("")
        print("Pengumuman : dikost ini bisa melakukan cicilan berdasarkan kategori")
    

def cicilan():
    harga1= "Rp 10.0000.0000"
    harga2= "Rp 8.000.000"
    harga3= "Rp 6.500.000"
    while True:
        daftarMatkul() 
        print("")   
        pilih= input("Masukkan Pilihan Kost Kategori Anda : ")
            
        if pilih=="1":
            print("Anda Memilih Kategori Premium, Selanjutnya")
            print("Anda Dapat Membayar Kost Dengan Cicilan Sebanyak 3 kali")
            print("dengan Total Pembayaran Semuanya Adalah ==>",harga1, "<== Pertahun")
            print("masukkan cicilan anda:")

            y=1
            total=0
            while (y<=3):
                cicilan=int(input("Bayar Cicilan Anda :  "))                                                                                                                                             
                total= total+cicilan
                y+=1
            print("")
            print("Jumlah Cicilan Yang Sudah Dibayar Adalah ",total)
            print("==> Cicilan Anda Sudah Selesai!!")
            print("")
            print("klik Enter Jika Ingin Kembali Kememu Awal")
            
            
        elif pilih=="2":
            print("Anda Memilih Kategori Exclusive, Selanjutnya")
            print("Anda Dapat Membayar Kost Dengan Cicilan Sebanyak 4 kali")
            print("dengan Total Pembayran Semuanya Adalah",harga2, "Pertahun")
            print("masukkan cicilan anda:")

            y=1
            total=0
            while (y<=4):
                cicilan=int(input("Bayar Cicilan Anda :  "))                                                                                                                                             
                total= total+cicilan
                y+=1
            print("")
            print("Jumlah Cicilan Yang Sudah Dibayar Adalah ",total)
            print("==> Cicilan Anda Sudah Selesai!!")
            print("")
            print("klik Enter Jika Ingin Kembali Kememu Awal")


        elif pilih=="3":
            print("Anda Memilih Kategori Reguler, Selanjutnya")
            print("Anda Dapat Membayar Kost Dengan Cicilan Sebanyak 6 kali")
            print("dengan Total Pembayran Semuanya Adalah",harga3, "Pertahun")
            print("masukkan cicilan anda:")

            y=1
            total=0
            while (y<=6):
                cicilan=int(input("Bayar Cicilan Anda :  "))                                                                                                                                             
                total= total+cicilan
                y+=1
            print("")
            print("Jumlah Cicilan Yang Sudah Dibayar Adalah ",total)
            print("==> Cicilan Anda Sudah Selesai!!")
            print("")
            print("klik Enter Jika Ingin Kembali Kememu Awal")
        else:
            print("Tdak ada Kategori tersebut di Kost Kami")

        os.system('pause')       
cicilan()
