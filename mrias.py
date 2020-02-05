class Tasit(): #parent
    def __init__(self,tekerSayisi,kapiSayisi):
        self.tekerSayisi = tekerSayisi
        self.kapiSayisi = kapiSayisi
        
    def kapiAc():
        print("kapı açıldı")


class Tir(Tasit):
    def __init__(self,tekerSayisi,kapiSayisi,turboSayisi):
        super().__init__(tekerSayisi,kapiSayisi)
        self.turboSayisi = turboSayisi
        
    def dorseBirak():
        print("dorse bırakıldı")
        

tir = Tir(4,2,1)
print(tir.kapiSayisi,tir.tekerSayisi,tir.turboSayisi)    
    
    
       