import mysql.connector
from prettytable import PrettyTable
import os

#Koneski database
db = mysql.connector.connect(
    host = 'localhost', #atau '127.0.0.1'
    user = 'root',
    password = '', 
    database = '5220411205'
)

class perusahaan:
    def __init__(self, nama_Perusahaan):
        self.nama_per =nama_Perusahaan

    def Get_perusahaan(self):
        return self.nama_per
    
class jabatan (perusahaan):
    def __init__(self, nama_Perusahaan,id_jabatan,Nama_jabatan):
        super().__init__(nama_Perusahaan)
        self.id = id_jabatan
        self.nama = Nama_jabatan

    def inputJabatan(self):
        connect = db.cursor()
        insert ="INSERT INTO jabatan(Nama_jabatan) VALUES (%s)"
        Nama_jabatan =input("Masukan Jenis Jabatan Yang ada di perusahaan :")
        connect.execute(insert,(Nama_jabatan,))
        db.commit()
        print("Data Berhasil Ditambahkan")

        
    def dataJabatan(self):
        connect= db.cursor()
        connect.execute("SELECT * FROM jabatan ")
        result = connect.fetchall()
        db.commit()
        tabel= PrettyTable(['id','Nama_jabatan',])
        tabel.add_rows(result)
        print(tabel)


class karyawan(perusahaan):
    def __init__(self, nama_Perusahaan,id_karyawan, Nama_Karyawan, id_Jabatan, Gaji, sandi):
         super().__init__(nama_Perusahaan)

    def update(self):
        conn=db.cursor()
        conn.execute("SELECT * FROM data_karywan")
        data= conn.fetchall()
        id=int(input("masukkan id pendaftar : ")) 
        for i in data:
            if id==i[0]:
                Bimbel = int(input("Anda Hanya Dapat Mengganti Sandi(1.sandi) :"))
                if Bimbel==1:
                    sandi = input("Masukkan sandi yang Baru :")
    
                else:
                    print("tidak ada Pilihan bimbel") 

                ganti="UPDATE data_karywan SET sandi=%s"
                ubah=[sandi]
                conn.execute(ganti,ubah)
                conn.fetchall()
                db.commit()    
                print("Data Yang dipilih Berhasil Di ganti".format(conn.rowcount))
                

class Admin(perusahaan):
    def __init__(self, nama_Perusahaan,id_karyawan, Nama_Karyawan, id_Jabatan, Gaji, sandi):
        super().__init__(nama_Perusahaan)
        self.id_karyawan = id_karyawan
        self.Nama_Karyawan = Nama_Karyawan
        self.id_Jabatan = id_Jabatan
        self.Gaji = Gaji
        self.sandi = sandi

    def dataKaryawan(self):
        connect= db.cursor()
        select_query = "SELECT id_karyawan, Nama_Karyawan, id_Jabatan, Gaji FROM data_karywan"
        connect.execute(select_query)
        result =connect.fetchall()
        db.commit()
        tabel= PrettyTable(['id','Nama Karyawan','id_Jabatan','gaji'])
        tabel.add_rows(result)
        print(tabel)

    def InputData(self):
        connect = db.cursor()
        insert = "INSERT INTO data_karywan (Nama_Karyawan,id_Jabatan,Gaji,sandi) VALUES(%s,%s,%s,%s)"
        Nama_Karyawan = input("Masukkan nama karyawan:")
        id_Jabatan = int(input("Masukkan Id_jabatan:"))
        Gaji = int(input("Masukkan Gaji karyawan:"))
        sandi = input("Masukkan sandi karyawan:")
        data= (Nama_Karyawan,id_Jabatan,Gaji,sandi,)
        connect.execute(insert,data)
        db.commit()
        print("Data Berhasil Ditambahkan")

    def cariData(self):
        connect = db.cursor()
        select = "SELECT id_karyawan, Nama_Karyawan, id_Jabatan FROM data_karywan"
        kode = int(input("Masukkan kode karyawan:"))
        connect.execute(select)
        karyawan = connect.fetchall()
        for i in karyawan:
            if i[0] == kode:
                print('='*20)
                print(f"Id Karyawan         : {i[0]}")
                print(f"Nama Karyawan       : {i[1]}")
                print(f"Id Jabatan          : {i[2]}")
                print('='*20)

        print('data berhasil ditampilkan'.format(connect.rowcount))

    def update(self):
        conn=db.cursor()
        conn.execute("SELECT * FROM data_karywan")
        data= conn.fetchall()
        id=int(input("masukkan id pendaftar : ")) 
        for i in data:
            if id==i[0]:
                Bimbel = int(input("Masukkan Jenis yang ingin diganti (1.id Jabatan 2.Gaji 3.Sandi) :"))
                if Bimbel==1:
                    id_jabatan = int(input("Masukkan Id Jabatan yang Baru :"))
                    ganti="UPDATE data_karywan SET id_jabatan=%s"
                    ubah=[id_jabatan]
                    conn.execute(ganti,ubah)
                    conn.fetchall()
                    db.commit()    
                elif Bimbel==2:
                    gaj = int(input("Masukkan Gaji yang Baru :"))
                    ganti="UPDATE data_karywan SET Gaji=%s"
                    ubah=[gaj]
                    conn.execute(ganti,ubah)
                    conn.fetchall()
                    db.commit()    
               
                else:
                    print("tidak ada Pilihan bimbel") 
                print("Data Yang dipilih Berhasil Di ganti".format(conn.rowcount))
            
    def delete(self):
        connect=db.cursor()
        id_karyawan=input("Masukkan No kode :")
        data=[id_karyawan]
        kirim="DELETE FROM data_karywan WHERE id_karyawan=%s"
        connect.execute(kirim,data)
        db.commit()
        print("Data Berhasil Dihapus")


#Inisialisasi
X= jabatan(0,0,0)
Y= karyawan(0,0,0,0,0,0)
Z= Admin(0,0,0,0,0,0)

def MenuJabatan():
    while True:
        print("="*20)
        print("1.Input jenis Jabatan")
        print("2.Data Jenis Jabatan")
        print("3.keluar")
        print("="*20)
        pilih = int(input("Masukkan pilihan :"))
        if pilih == 1:
            X.inputJabatan()
        elif pilih == 2:
            X.dataJabatan()
        elif pilih == 3:
            break
        else :
            print('Menu Tidak Terdaftar')
def menuAdmin():
    while True:
        print("="*20)
        print("1.Input data karyawan")
        print("2.Lihat Data semua karyawan")
        print("3.Cari Karyawan")
        print("4.keluar")
        print("="*20)
        pilih = int(input("Masukkan pilihan :"))
        X.dataJabatan()
        if pilih == 1:
            Z.InputData()
        elif pilih == 2:
            Z.dataKaryawan()
        elif pilih == 3:
            Z.cariData()
        elif pilih == 4:
            break
        else :
            print('Menu Tidak Terdaftar')

def MenuKaryawan():
    conn = db.cursor()
    conn.execute("SELECT * FROM data_karywan")
    result = conn.fetchall()
    # print(e)
    name = input("Masukkan username:")
    password = input("Masukkan password:")    
    for i in result:
        if name == i[1] and password == i[4] :
            print("="*25) 
            print(f"Login atas nama {i[1]} Dengan Id Jabatan {i[2]}")
            print("="*25)
            while True:
                print("="*20)
                print("1.Lihat Gaji")
                print("2.Lembur")
                print("3.Update Password")
                print("4.Keluar")
                print("="*20)
                login = int(input("Masukkan pilihan:"))
                if login == 1:
                    print("="*25)
                    print(f"Gaji pokok {name} sebagai {i[2]} adalah : {i[3]}")
                    print("="*25)
                elif login == 2:
                    jam = int(input("Masukkan jam lembur:"))
                    lembur = jam *10000
                    hasil = lembur + i[3]
                    print("="*25)
                    print(f"Total gaji {name} sebagai {i[2]} ditambah lembur {jam} jam : {hasil}")
                    print("="*25)
                elif login == 3:
                    Y.update()
                elif login == 4: 
                    break
                else :
                    print('Menu Tidak Terdaftar')


while True: 
    os.system ('cls')
    print("="*20)
    print("PT.SUKA CITA")
    print("="*20)
    print("1.Login sebagai Admin")
    print("2.Login sebagai Karyawan")
    print("3.Keluar")
 
    login = int(input("Masukkan pilihan login:"))
    if login == 1:
        sandi = input("Masukkan sandi:")
        if sandi == "sukacita":
            while True:
                print("="*20)
                print("1. Jenis Jabatan")
                print("2. Data Karyawan")
                print("3.keluar")
                print("="*20)
                pilih = int(input("Masukkan pilihan :"))
                if pilih == 1:
                    MenuJabatan()
                elif pilih == 2:
                    menuAdmin()
                elif pilih == 3:
                    break
                else :
                    print('Menu Tidak Terdaftar')
        else:
            print("Sandi Yang dimasukkan Salah")
    elif login ==2 :
        MenuKaryawan()
    elif login ==3 :
        break
    else :
        print('Menu Tidak Terdaftar')
    os.system('pause')
