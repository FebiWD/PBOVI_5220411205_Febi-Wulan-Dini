

class matkul:
    matkul1 = None
    _matkul2 = None
    __matkul3 = None

    def __init__ (self, x,y,z):
        self.matkul1 = x
        self._matkul2 = y
        self.__matkul3 = z
    
    def __tiga(self):
        print ("mata kuliah ketiga adalah", self.__matkul3)

    def akses(self):
        self.__tiga()

# var =matkul("PBO", "PAD","OOP")
# print("matkul pertama adalah :", var.matkul1)
# print("matkul pertama adalah :", var._matkul2)
# var.akses()


class Nilai(matkul):
    def __init__ (self,x,y,z,q):
        super().__init__ (x,y,z)
        self.nilai2 = q
        
    # def aksesNilai(self):
    #     self.__tiga()

    def _dua(self):
        print( "ini adalah nilai darimatkul PBO :", self._matkul2)

    

nilai=Nilai(80,80,100,100)
print("ini adalah nilai dari matkul sisbil :", nilai.matkul1)
nilai._dua()
nilai.akses()
print("ini adalah nilai dari matkul PAD :", nilai.nilai2)


    
