## Class Orang Tua
class camera:
    jenis = None ## Public
    __tarif = None ## Private
    def __init__ (self, jenisKamera, tarifSewa):
        self.jenis = jenisKamera
        self.__tarif = tarifSewa

    ## function pemanggilan Acces private
    def akses(self):
        print ("harga sewa perhari adalah : ", self.__tarif)
        return self.__tarif
   

## class Turunan dari camera  
class Jenis(camera):
    def __init__ (self,jenisKamera, tarifSewa):
        super().__init__(jenisKamera, tarifSewa)

## Funtion Menu
def menu():
    while True:
        print("""
            Selamat Datang Di Rental Camera Kami

                =============== Jenis-Jenis Kamera ===============
                1. DSLR
                2. Mirrorless
                3. Action Cam
                =====================================================
                """)
        
        pilih= int(input("Masukkan Jenis Kamera Yang Ingin Anda Sewa (1-3) :"))

        if pilih == 1:
            print("Jenis Kamera Dan Ketentuan harga Sewa Perharinya adalah :")
            y= Jenis("DSLR", 200000) 
            print("jenis kamera adalah :",y.jenis), y.akses()
            print("")
            sewa=input("Apakah Anda Ingin Melanjutkan Menyewa (Y/N) :")
            if sewa== "Y":
                hari= int (input("Masukkan Jumlah Hari anda Ingin Menyewa :"))
                print("Biaya Sewa Anda Adalah : Rp.",hari * y.akses())
            else:
                print("Anda Memilih Tidak Menyewa Kamera Ini")
                break
            
        elif pilih == 2:
            print("Jenis Kamera Dan Ketentuan harga Sewa Perharinya adalah :")
            y= Jenis("Mirroless", 300000) 
            print("jenis kamera adalah :",y.jenis), y.akses()
            print("")
            sewa=input("Apakah Anda Ingin Melanjutkan Menyewa (Y/N) :")
            if sewa== "Y":
                hari= int (input("Masukkan Jumlah Hari anda Ingin Menyewa :"))
                print("Biaya Sewa Anda Adalah : Rp.",hari * y.akses())
            else:
                print("Anda Memilih Tidak Menyewa Kamera Ini")
                break
        
        elif pilih == 3:
            print("Jenis Kamera Dan Ketentuan harga Sewa Perharinya adalah :")
            y= Jenis("Action Cam", 350000) 
            print("jenis kamera adalah :",y.jenis), y.akses()
            print("")
            sewa=input("Apakah Anda Ingin Melanjutkan Menyewa (Y/N) :")
            if sewa== "Y":
                hari= int (input("Masukkan Jumlah Hari anda Ingin Menyewa :"))
                print("Biaya Sewa Anda Adalah : Rp.",hari * y.akses())
            else:
                print("Anda Memilih Tidak Menyewa Kamera Ini")
                break
        else:
            print("Pilihan Tidak Ada Dimenu")    
        break

# Pemanggilan Program
menu()
print("Terima Kasih Telah Memilih Kami")
