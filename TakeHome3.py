import os
os.system ('cls')
class mandiri:
    def __init__(self,x,y,z,v):
        self.namaLayanan= x
        self.JenisLayanan= y
        self.lamaLayanan= z
        self.gaji = v
    
    def nama_layanan(self):
        print("""======================= Nama Layanan =================
            1. Asuransi
            2. Deposit
            3. Investasi
              """)
        print(60*'=')
        print("")
        pilih= int(input("masukkan layanan yang anda pilih :"))
        if pilih==1:
            run.jenis_layanan()
        elif pilih==2:
            run.jenis_layanan()
        elif pilih==3:
            run.jenis_layanan()
        else:
            print("layanan tersebut tidak ada")
        
        self.namaLayanan= pilih
        return pilih
        
    def jenis_layanan(self):
        print("""======================= Jenis Layanan ================
            1. Diamond ==> 20.000.000
            2. Gold    ==> 15.000.000
            3. Silver  ==> 10.000.000
              """)
        print(60*'=')
        print("")
        jenis= int(input("Masukkan  jenis Layanan yang anda pilih :"))
        if jenis==1:
            run.lama_langganan()
            print(" Diamond ==> 20.000.000")
        elif jenis==2:
            run.lama_langganan()
            print(" Gold    ==> 15.000.000")
        elif jenis==3:
            run.lama_langganan()
            print(" Silver  ==> 10.000.000")
        else:
            print("Yang Anda Masukkan Salah")
         
        self.namaLayanan= jenis
        return jenis
        
    def lama_langganan(self):
        print("""======================= Lama Langgnan ================
            1. 6 bulan
            2. 1 tahun
            3. 2 tahun
              """)
        print(60*'=')
        print("")
        lama= int(input("Masukkan Lama Langganan yang anda pilih :"))
        if lama==1:
            print("Selamat anda berlangganan selama 6 Bulan")
        elif lama==2:
             print("Selamat anda berlangganan selama 1 Tahun")
        elif lama==3:
             print("Selamat anda berlangganan selama 2 Tahun")
        else:
            print("Yang Anda Masukkan Salah")
          
        self.namaLayanan= lama
        return lama
    
    def range(self):
        print("")
        nama =input ("masukkan nama anda :")
        print("""
        ========== Range Penghasilan Nasabah ==========
        1. Penghasilan > 500jt = bisa memilih 3 layanan
        2. Penghasilan 100 - 500 juta = bisa memilih 2 memilih
        3. Penghasilan < 100 juta = bisa memilih 1 layanan
        """)
        print(60*'=')
        self.gaji = nama
        return nama
    
    def penghasilan(self):
        while True:
            run.range()
            penghasilan= int(input("Masukkan penghasilan anda perbulannya yang anda pilih :"))
            if penghasilan ==1:
                print("Anda Dapat Melakukan Layanan sebanyak 3 kali")
                a = 1
                total= 0
                while(a<=3):
                    run.nama_layanan()
                    harga = int(input("Masukkan harga layanan yang Anda Pilih: "))
                    total = total + harga
                    a += 1
                    print("total pembayaran anda adalah :",total)
                
            elif penghasilan ==2:
                print("Anda Dapat Melakukan Layanan sebanyak 2 kali")
                a = 1
                total =0
                while(a<=2):
                    run.nama_layanan()
                    harga = int(input("Masukkan harga layanan yang Anda Pilih: "))
                    total = total + harga
                    a += 1
                    print("total pembayaran anda adalah :",total)
                     
            elif penghasilan == 3:
                print("Anda Dapat Melakukan Layanan sebanyak 3 kali")
                a = 1
                total=0
                while(a<=1):
                    run.nama_layanan()
                    harga = int(input("Masukkan harga layanan yang Anda Pilih: "))
                    total = total + harga
                    a += 1
                    print("total pembayaran anda adalah :",total)
                
            else:
                print("TIDAK ADA MENU TERSEBUT DILAYANAN KAMI")
                
            break       
# pemangglan            
run =mandiri (0,0,0,0)
run. penghasilan()
print("")
print("TERIMAH KASIH")


    

