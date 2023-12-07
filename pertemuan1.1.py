print("PEMILIHAN PRESIDEN DI NEGERI KONOHA")
Nik = (input("Masukkan Nik Anda Terlebih Dahulu :"))

def konoha():
    if len (Nik)==12:
        print("Anda Berhasil Masuk Kedalam Menu")
      
        print("Daftar Nama Capres :")
        print("1. Uzumaki Nanito")
        print("2. Gojo Sotoru")
        print("3. Yu Nishinoya")
        while True:   
            pilihan =int(input("Silahkan Memilih Capres mu :"))

            if pilihan == 1:
                print( "  =Pilihan anda Uzumaki Nanito= ")
                break
            elif pilihan == 2:
                print(" =Pilihan Anda Gojo Sotoru= ")
                break
            elif pilihan == 2:
                print(" =Pilihan Anda Yu Nishinoya= ")
                break
            else:
                print("Tidak Terdaftar Dalam Pemilu")
        print("Terimah kasih Sudah Memilih")
    else:
        print("Nik tidak Terdaftar")       
       
konoha()
