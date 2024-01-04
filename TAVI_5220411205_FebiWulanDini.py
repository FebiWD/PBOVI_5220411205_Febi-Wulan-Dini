
import datetime

#class induk
class Kendaraan:
    def __init__(self,_jenisKendaraan, _waktuTerkahirServis):
        self.jenis = _jenisKendaraan
        self.waktu = _waktuTerkahirServis
      
    def input(self):
        jenis= input( "jenis kendaraan : ")
        jenis = self.jenis
        return jenis
    
    def servis_berikutnya(self):
        self.waktu= input("Tanggal Terakhir Servis (YYYY-MM-DD): ")

    #overloading    
    def servis_berikutnya(self):
        self.waktu= input("Tanggal Terakhir Servis (YYYY-MM-DD): ")
        last_service_date = datetime.datetime.strptime(self.waktu, "%Y-%m-%d").date()
        next_service_date = last_service_date + datetime.timedelta(days=90)
        print("Tanggal selanjutnya servis: ", next_service_date)
        return next_service_date,next_service_date
    
    def servis(self):
        print("Melakukan servis umum.")

#class Mobil  turunan dari class kendaraan
class Mobil(Kendaraan):
    def __init__(self, _jenisKendaraan, _waktuTerkahirServis, merk, tahunProduksi):
        super().__init__(_jenisKendaraan, _waktuTerkahirServis)
        self.merk = merk
        self.tahun = tahunProduksi

    def datamobil(self):
        merk = input("Merk Mobil: ")
        produksi = input("Tahun Produksi: ")
        merk=self.merk
        produksi=self.tahun
        return merk, produksi

    #overriding 
    def servis(self):
        print("Melakukan servis khusus mobil.")

#class Mobil Konvesional turunan dari class mobil    
class MobilKonvensional(Mobil):
    def __init__(self, _jenisKendaraan, _waktuTerkahirServis, merk, tahunProduksi, konsumsi_bahan_bakar):
        super().__init__(_jenisKendaraan, _waktuTerkahirServis, merk, tahunProduksi)
        self.bahan_bakar = konsumsi_bahan_bakar

    def data_mobil_konvensional(self):
        bahan_bakar = input("Konsumsi Bahan Bakar (km/liter): ")
        bahan_bakar = self.bahan_bakar
        return bahan_bakar
    
    def servis(self):
        print("servis Mobil Berlangsung")
        print("servis Mobil Selesai")

#class Mobil listrik turunan dari class mobil
class MobilListrik(Mobil):
    def __init__(self, _jenisKendaraan, _waktuTerkahirServis, merk, tahunProduksi, kapasitas_baterai):
        super().__init__(_jenisKendaraan, _waktuTerkahirServis, merk, tahunProduksi)
        self.kapasitas = kapasitas_baterai

    def data_mobil_listrik(self):
        baterai = input("Kapasitas Baterai (kWh): ")
        baterai = self.kapasitas
        return baterai
        
    def servis(self):
        print("servis Mobil Berlangsung")
        print("servis Mobil Selesai")

#class Motor turunan dari kendaraan
class Motor(Kendaraan):
    def __init__(self, _jenisKendaraan, _waktuTerkahirServis, merek, tahun_pembuatan, kapasitas_mesin):
        super().__init__(_jenisKendaraan, _waktuTerkahirServis)
        self.merek = merek
        self.tahun = tahun_pembuatan
        self.kapasitas= kapasitas_mesin

    def data_motor(self):
        merk = input("Merk Motor: ")
        produksi = (input("Tahun Produksi: "))
        kapsitas = input("Kapasitas Mesin (cc): ")

        merk=self.merek
        produksi=self.tahun
        kapsitas =self.kapasitas

        return merk, produksi, kapsitas

    def servis(self):
        print("servis Motor Berlangsung")
        print("servis Motor Selesai")
    
#inisialisasi
X = Kendaraan(0,0)
Y=Mobil(0,0,0,0)
Z=MobilKonvensional(0,0,0,0,0)
A= MobilListrik(0,0,0,0,0)
B= Motor(0,0,0,0,0)

#Menu untuk pemilihan Servis Mobil Konvesional
def servisMobilK():
    print("")
    print("""=========== layanan servis Mobil Konvesional ============
            1.Servis Berkala --> 300.000
            2.Servis Tune Up --> 250.000
            3.Servis Jok Mobil" --> 200.000   
=======================================================""")
    jenis = input("Masukan Pilihan Anda: ")
    if jenis == "1":
        print("Anda Memilih Servis Berkala Dengan Harga --> Rp.300.000")
        pilih = input("Lanjutkan ke Proses Servis (y/n):")
        if pilih =='y':
            X.servis_berikutnya()
            Z.servis()
        elif pilih =='n':
            print("servis tidak dilakukan")
        else:
            print("pilihan tidak ada dimenu")   

    elif jenis == "2" :
        print("Anda Memilih Servis Tone Up Dengan Harga --> Rp.250.000")
        pilih = input("Lanjutkan ke Proses Servis (y/n):")
        if pilih =='y':
            X.servis_berikutnya()
            Z.servis()
        elif pilih =='n':
            print("servis tidak dilakukan")
        else:
            print("pilihan tidak ada dimenu")

    elif jenis == "3" :
        print("Anda Memilih Servis Jok Mobil Dengan Harga --> Rp.200.000")
        pilih = input("Lanjutkan ke Proses Servis (y/n):")
        if pilih =='y':
            X.servis_berikutnya()
            Z.servis()
        elif pilih =='n':
            print("servis tidak dilakukan")
        else:
            print("pilihan tidak ada dimenu")
    else:
        print("Tidak Ada Dipilihan")

#Menu untuk pemilihan Servis Mobil Listrik
def servisMobilL():
    print("")
    print("""=========== layanan servis Mobil Listrik ============
            1. Servis Berkala ---> 300.000")
            2. Servis Baterai ---> 200.000")   
=====================================================""")
    jenis = input("Masukan Pilihan Anda: ")
    if jenis == "1":
        print("Anda Memilih Servis Berkala Dengan Harga --> Rp.300.000")
        pilih = input("Lanjutkan ke Proses Servis (y/n):")
        if pilih =='y':
            X.servis_berikutnya()
            A.servis()
        elif pilih =='n':
            print("servis tidak dilakukan")
        else:
            print("pilihan tidak ada dimenu")   

    elif jenis == "2" :
        print("Anda Memilih Servis Baterai Dengan Harga --> Rp.200.000")
        pilih = input("Lanjutkan ke Proses Servis (y/n):")
        if pilih =='y':
            X.servis_berikutnya()
            A.servis()
        elif pilih =='n':
            print("servis tidak dilakukan")
        else:
            print("pilihan tidak ada dimenu")
    else:
        print("Tidak Ada Dipilihan")

#Menu untuk pemilihan servis Motor
def servisMotor():
    print("")
    print("""=========== layanan servis Mobil Listrik ============
            1. Servis Motor Ringan ---> 100.000")
            2. Servis Motor Berat ---> 200.000")   
        """)
    jenis = input("Masukan Pilihin Anda: ")

    if jenis == "1":
        print("Anda Memilih Servis Motor Ringan Dengan Harga --> Rp.100.000")
        pilih = input("Lanjutkan ke Proses Servis (y/n):")
        if pilih =='y':
            X.servis_berikutnya()
            B.servis()
        elif pilih =='n':
            print("servis tidak dilakukan")
        else:
            print("pilihan tidak ada dimenu")   

    elif jenis == "2" :
        print("Anda Memilih Servis Motor Berat Dengan Harga --> Rp.200.000")
        pilih = input("Lanjutkan ke Proses Servis (y/n):")
        if pilih =='y':
            X.servis_berikutnya()
            B.servis()
        elif pilih =='n':
            print("servis tidak dilakukan")
        else:
            print("pilihan tidak ada dimenu")
    else:
        print("Tidak Ada Dipilihan")
    print("Terima Kasih Sudah Menggunkan Layanan kami")    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#Menu untuk pemilihan Jenis Mobil
def jenis1():
    print("")
    print("""            Jenis Mobil 
            1. Mobil Konvesional
            2. Mobil Listrik
    """)
    jenis = input("Masukan Jenis Kendaraan: ")
    if jenis == "1":
        print("Silahkan Masukan Data Mobil Terlebih Dahulu")
        Z.datamobil()
        Z.data_mobil_konvensional()   

        print("--> silhakan memilih layanan servis yang dinginkan <---")
        servisMobilK()

    elif jenis == "2" :
        print("Silahkan Masukan Data Mobil Terlebih Dahulu")
        A.datamobil()
        A.data_mobil_listrik   

        print("--> silhakan memilih layanan servis yang dinginkan <---")
        servisMobilL()
    else:
        print("Tidak Ada Dipilihan")
    print("Terima Kasih Sudah Menggunkan Layanan kami")    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    

#Menu untuk pemilihan Jenis kendaraan
def jenis2():
    jenis = input("Masukan Jenis Kendaraan: ")
    if jenis == "1":
       jenis1

    elif jenis == "2" :
        print("Silahkan Masukan Data Mobil Terlebih Dahulu")
        B.data_motor()
        servisMotor()
    elif jenis =="3":
        exit()
    else:
        print("Tidak Ada Dipilihan")

#     print(">>>>>>>>>>>>>>>TERIMA KASIH >>>>>>>>>>>>>>>>>")

# #Tampilan Utama
while True:
 
    print(">>>>>>>>>>>>>>> SELAMAT DATANG DI SERVIS BUDI UTAMI >>>>>>>>>>>>>>>>>")
    print()
    print("""             Jenis Kendaraan 
            1. Mobil
            2. Motor
            3. exit
    """)
   
    jenis2()
    jenis1()
    print(">>>>>>>>>>>>>>>TERIMA KASIH >>>>>>>>>>>>>>>>>")
