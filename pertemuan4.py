#MENENTUKAN IPKK BERDASRKAN NILAI DARI MATKU

class ipk:
    def __init__ (self,a,b,c,d):
        self.nilai11 = a
        self.nilai2 = b
        self. matkul1 = c
        self.matkul2 = d
    
    def Nmatkul (self):
        pertama = input (" Masukkan Nama Mata Kuliah Pertama :")
        sks=int(input(" Masukkan JUmalah SKS pada Matkul PEmrograman Berorientasi Objek (1-3) :"))
        nilai1= int(input(" Masukkan NIlai Dari Matkul Tersebut (0-100)  :"))
        if nilai1 <= 100 and nilai1 > 80 :
            bobot = 4
            print("==>Bobot Nilai Anda Adalah A <==")
        elif nilai1 <= 80 and nilai1 > 60:
            print("==>Bobot Nilai Anda Adalah B <==")
            bobot = 3
        elif nilai1 <= 60 and nilai1 > 35:
            print("==>Bobot Nilai Anda Adalah C <==")
            bobot = 2
        elif nilai1 <= 35 and nilai1 > 20:
            print("==>Bobot Nilai Anda Adalah D <==")
            bobot = 1
        elif nilai1 <= 20 and nilai1 > 0:
            print("==>Bobot Nilai Anda Adalah E <==")
            bobot = 0
            
        nilai1=self.nilai2
        pertama= self.matkul1
        self.sks = sks
        total = bobot * sks
        print ("Bobot Pada MataKuliah Pemrograman Berorientasi objek adalah :",total)
        return total
        
    def Nmatkul2 (self):
        kedua = input (" \nMasukkan Nama Mata Kuliah Kedua :")
        sks2=int(input(" Masukkan JUmalah SKS pada Matkul PEmrograman Berorientasi Objek (1-3) :")) 
        nilai= int(input(" Masukkan NIlai Dari Matkul Tersebut(0-100)  :"))
        if nilai <= 100 and nilai > 80:
            print("==>Bobot Nilai Anda Adalah A <==")
            Bobot = 4
        elif nilai <= 80 and nilai > 60:
            print("==>Bobot Nilai Anda Adalah B <==")
            Bobot = 3
        elif nilai <= 60 and nilai > 35:
            print("==>Bobot Nilai Anda Adalah C <==")
            Bobot = 2
        elif nilai <= 35 and nilai > 20:
            print("==>Bobot Nilai Anda Adalah D <==")
            Bobot = 1
        elif nilai <= 20 and nilai > 0:
            print("==>Bobot Nilai Anda Adalah E <==")
            Bobot = 0
        nilai=self.nilai11
        kedua= self.matkul2
        self.sks2 = sks2
        total1 = Bobot * sks2
        print ("Bobot Pada MataKuliah Pemrograman Berorientasi objek adalah :",total1)
        return total1
        
    def Total (self):
        totalbs= self.Nmatkul() + self.Nmatkul2()
        totalsks= self.sks + self.sks2
        print("\n Total Semua Bobot Nilai :",totalbs)
        print("Total Semua Sks Anda Adalah :",totalsks)

        ipk= totalbs/totalsks
        print("\n Ipk Anda  Anda Adalah :",ipk)
        
        
# pemanggilan 
jalan= ipk(0,0,0,0)
nama =input("\n  Masukkan NPM Anda :")
print(""" ++++++++++++++++++++ Daftar Mata Kuliah ++++++++++++++++++++
              1. Pemrograman Berbasis Objek ==> PBO
              2. Pengantar Anlisis Data ==> PAD
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      """)
jalan.Total()

