


print("PEMILIHAN KONSENTARSI BERDASARKAN NILAI DARI MATKUL PBO ")
print("Skala NIlai 10-100")
Nama = int(input ("NPM Mahasiswa :"))
Nilai= int (input ( "Nilai Dari Matkul Statistika :"))

def Kosentrasi():
    if Nilai > 75:
        print("Anda Masuk kedalam Konsetrasi Web & Mobile")
    elif Nilai < 75:
        print("Anda Masuk kedalam Konsetrasi Kosentarsi Sistem Cerdas")
    else:
        print("Anda Salahkan Memasukann Nilai")

Kosentrasi()



     
