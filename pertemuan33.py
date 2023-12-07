
class Bidang:

    def __init__(self, a , b, c):
        self.xx = a
        self.xy = b
        self.yy = c
    def hitungLuas(self):
        luas = self.xx * self.xy * self.yy
        return luas
    def bintang():
        print("*" *15)


sisi= int(input("masukkan sisi/lebar :"))
panjang = int(input("masukkan panjang :"))
jari = int(input("masukkan jari2 :"))

Bidang.bintang()

persegi = Bidang(sisi,sisi,1)
persegiPanjang = Bidang(panjang, sisi,1)
segi2 = Bidang (panjang,sisi,0.5)
lingkaran= Bidang(jari,jari,3.14)

print("Luas Persegi",persegi.hitungLuas())
print("Luas Persegi Panjang",persegiPanjang.hitungLuas())
print("Luas Segitiga",segi2.hitungLuas())
print("Luas Lingkaran",lingkaran.hitungLuas())

Bidang.bintang()