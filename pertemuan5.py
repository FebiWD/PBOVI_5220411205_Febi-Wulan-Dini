#MODIFIER
class Hewan :
    var1 = None     #Public
    _var2= None     #Prorected
    __var3 = None   #Private

    def __init__(self,var1,var2,var3) :
       
        self.var1= var1
        self._var2 = var2
        self.__var3= var3

    def __display(self):
        print("Ini menampilkan variabel 3:", self.__var3)


    def akses(self):
        self.__display()

# x=Hewan("Singa", "Harimau","Kucing")
# print("Ini Hewan:", x.var1)
# print("Ini Hewan Kedua:", x._var2)
# x.akses()
# print("Ini Hewan Ketiga:", x._Hewan__var3)  #CaraPeratama

#INHERITANCE(PEWARISAN)
class HewanDiLindungi(Hewan):
    def __init__(self,var1,var2,var3,var4) :
        super().__init__(var1,var2, var3)
        self.var4= var4

    def aksesanak(self):
        self.__display()
        
y = HewanDiLindungi("Anoa","Harimau Sumatera","Badak Cula Satu", "Cendrawasih")
print("Hewan Yang dilindungi :", y.var1)
print("Hewan Yang dilindungi :", y._var2)
y.akses()
print("Hewan Yang dilindungi :", y.var4)