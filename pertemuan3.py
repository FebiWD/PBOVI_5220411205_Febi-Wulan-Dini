def jenis():
    print("")
    print("================ Jenis Layanan ===============")
    print(" 1. Investasi  ")
    print(" 2. Kartu Kredit ")
    print(" 3. Deposit ")
    print(" 4. Asuransi ")

    layanan= input("silahkan Masukkan layanan yang anda pilih :")
    if layanan=='1':
        print("Anda Memilih Investasi ")
        print("Anda Dapat Melakukan Pembayaran Minimal Sebesar Rp10.000000")
        
    elif layanan=='2':
        print("Anda Memilih Kartu Kredit ")
        print("Anda Dapat Melakukan Pembayaran Minimal Sebesar Rp.1000000")
    elif layanan=='3':
        print("Anda Memilih Deposit ")
        print("Anda Dapat Melakukan Pembayaran Minimal Sebesar Rp.5000000")
    elif layanan=='4':
        print("Anda Memilih Asuransi ")
        print("Anda Dapat Melakukan Pembayaran Minimal Sebesar Rp.500000")
    else:
        print("Kami Tidak Menyediakan Layanan Tersebut ")


def namaLayanan():
    print("")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("     Selamat Datang Di Layanan Bank Mandiri      ")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("================ Nama Layanan ===============")
    print(" 1. Layanan Platinum ")
    print(" 2. Layanan Diamond ")
    print(" 3. Layanan Gold ")
    print(" 4. Layanana Silver ")
     
    layanan= input("silahkan Masukkan layanan yang anda pilih :")
    if layanan=='1':
        print("Anda Memilih Layanan Platinum ")
        lama = input ("berapa lama anda berlanganan dilayanan ini :")

    elif layanan=='2':
        print("Anda Memilih Layanan Diamond ")
        lama = input ("berapa lama anda berlanganan dilayanan ini :")

    elif layanan=='3':
        print("Anda Memilih Layanan Gold ")
        lama = input ("berapa lama anda berlanganan dilayanan ini :")
    
    elif layanan=='4':
        print("Anda Memilih Layanan Silver ")
        lama = input ("berapa lama anda berlanganan dilayanan ini :")

    else:
        print("Kami Tidak Menyediakan Layanan Tersebut ")
    
    jenis()
    

nama= input("Masukkan Nama Anda :")
def layanan():
    while True:
        print("""
        ========== Range Penghasilan Nasabah ==========
        1. Penghasilan > 500jt = bisa memilih 3 layanan
        2. Penghasilan 100 - 500 juta = bisa memilih 2 memilih
        3. Penghasilan < 100 juta = bisa memilih 1 layanan
        =======================================
        """)
        gaji= (input("Berapa Penghasilan Anda :"))

        if gaji =='1':
            print("Anda Dapat Melakukan Layanan sebanyak 3 kali")
            a = 1
            total = 0
            while(a<=3):
                namaLayanan()
                harga = int(input("Masukkan harga layanan yang Anda Pilih: "))
                total = total + harga
                a += 1
                print("total pembayaran anda adalah :",total)

        elif gaji =='2':
            print("Anda Dapat Melakukan Layanan sebanyak 2 kali")
            a = 1
            total = 0
            while(a<=2):
                namaLayanan()
                harga = int(input("Masukkan harga layanan yang Anda Pilih: "))
                total = total + harga
                a += 1
                print("total pembayaran anda adalah :",total)

        elif gaji =='3':
            print("Anda Dapat Melakukan Layanan sebanyak 1 kali")  
            a = 1
            total = 0
            while(a<=1):
                namaLayanan()
                harga = int(input("Masukkan harga layanan yang Anda Pilih: "))
                total = total + harga
                a += 1 
                print("total pembayaran anda adalah :",total)

        else:
            print("Anda Salah Memasukan Range Penghasilan")
layanan()

