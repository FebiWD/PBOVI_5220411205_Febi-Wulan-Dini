
class Katalog:
    def cari ():
        print("apakah anda ingin mencari sebuah katalog?")

        
class Perpustelem:
    def __init__ (self, judul, subjek):
        self.jdl = judul
        self.sub = subjek

    def LokasiPenyimpanan(self):
        a= input("Pilhan antara Judul atau subjek :")
        if a =="judul":
            jud = input("masukkan judul dari sebuah buku/majalah/dvd :")
            jud= self.jdl
            return jud
    
        elif a== "subjek":
            subjk = input("masukkan judul dari sebuah buku/majalah/dvd :")
            subjk= self.sub
            return subjk
        
    def info (self):
        print ("Info Lebih lanjut Tentang Buku / Majalah / DVD")


class Buku(Perpustelem):
    def __init__ (self,judul, subjek , ISBN, Pengaras, jmlHal, ukuran):
        super().__init__(judul, subjek)
        self.jumlah = jmlHal
        self.isb = ISBN
        self.ukur = ukuran
        self.pgrng = Pengaras

    def info(self):
        z= input("apakah anda ingin mengetahui lebih lanjut (y/n): ")
        if z == "y" :
            isbn = 234567890234
            hal= 70
            pengrg ="Velen shinta"
            ukrn= "A4"
            isbn= self.isb , hal= self.jumlah , pengrg = self.pgrng , ukrn = self.ukur
            print ("ISBN:", isbn , "Pengarang :", pengrg, "Ukuran :",ukrn, "jumlah halaman :", hal )

        elif z== "n":
            print("anda memilih untuk melihat lebih lanjut.")
        
        else:
            print("anda memilih menu yang salah")

class Majalah(Perpustelem):
    def __init__ (self,judul, subjek , volume , issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issu = issue
       

    def info(self):
        z= input("apakah anda ingin mengetahui lebih lanjut (y/n): ")
        if z == "y" :
            isbn = 345555
            hal= 70
           
            isbn= self.isb , hal= self.jumlah , pengrg = self.pgrng , ukrn = self.ukur
            print ("ISBN:", isbn , "Pengarang :", pengrg, "Ukuran :",ukrn, "jumlah halaman :", hal )

        elif z== "n":
            print("anda memilih untuk melihat lebih lanjut.")
        
        else:
            print("anda memilih menu yang salah")
