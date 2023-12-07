class coba:
    def __init__(self,x2,x3):
        self.x1 = 5
        self.xx2 = x2
        self.xx3 = x3

    def terbesar(self,a,b,c):
        if self.x1>b and self.x1>c:
            max = a
        elif b>a and b>c:
            max = b
        elif c>self.x1 and c>b:
            max = c
        return min
    
nil2= 10
nil3=10

bidang = coba(nil2,nil3)

print("angka terbesar ", bidang.terbesar(bidang.x1,nil2,nil3))
    