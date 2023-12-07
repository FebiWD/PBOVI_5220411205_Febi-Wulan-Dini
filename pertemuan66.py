
class sales:
    def __init__(self, nama, target):
        self.nama = nama
        self.tar= target

    def lihat(self):
        print("Nama Sales",self.nama, "target penjulan ", self.tar)

    def lihat(self,jum):
        if jum > 10:
            total = jum
            print("Nama Sales",self.nama, "Target prnjualan", self.tar," total penjualan",total,"terpenuhi")

        else:
            total = jum
            print("Nama Sales",self.nama, "Target prnjualan", self.tar," total penjualan",total,"Tidak Terpenuhi")

class bulan(sales):
    def __init__ (self, nama, target,bln):
        super().__init__(nama, target)
        self.bul= bln

    def lihat(self,jum):
        if jum > 10:
            total = jum
            print("Nama Sales",self.nama, "Target prnjualan", self.tar,"pada Bulan ", self.bul ,"total penjualan",total,"terpenuhi")

        else:
            total = jum
            print("Nama Sales",self.nama, "Target prnjualan", self.tar,"pada Bulan ", self.bul ," total penjualan",total,"Tidak Terpenuhi")


x= sales("febi", 10)
x.lihat(0)
x.lihat(11)

print("")
x2=bulan("febi", 10,"Oktober")
x2.lihat(0)
x2.lihat(15)
        