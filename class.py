"""
class Asker():
    saglik = 100
    isim = "ahmet"
    silah = "tüfek"


print(Asker.saglik)

Asker.mermiSayisi = 100

print(Asker.mermiSayisi)
"""
#%%
"""
class Siparis():
    firmalar = []
    miktar = 0
    tarih = ""
    
    
gofret = Siparis()
gofret.firmalar += ["ülker"]
gofret.miktar = 1000
gofret.tarih = "12.12.2018"

kitap = Siparis()
kitap.firmalar += ["can yayınları"]
kitap.miktar = 10000
kitap.tarih = "10.10.2018"


print(gofret.firmalar)
print(gofret.miktar)
print(gofret.tarih)
print()

print(kitap.firmalar)
print(kitap.miktar)
print(kitap.tarih)
"""
#%%
"""
class Asker():
    
    def __init__(self):
        self.kabiliyetleri = []
        print("deneme")
  
  
ahmet = Asker()
#mehmet = Asker()
#
#ahmet.kabiliyetleri += ["123"]
#mehmet.kabiliyetleri += ["asdasd"]
#
#print(ahmet.kabiliyetleri)

class Deneme():
    print("alfabe")
"""
#%%

class Asker():
    kabiliyetler = []    
    def __init__(self,isim,guc):
        self.isim = isim
        self.gucu = guc
        self.kabiliyetler = []

ahmet = Asker("ahmet",80)
mehmet = Asker("mehmet",60)

ahmet.kabiliyetler += ["nişancı"]
mehmet.kabiliyetler += ["tank"]


print(ahmet.isim)
print(ahmet.gucu)
print(ahmet.kabiliyetler)
print(mehmet.kabiliyetler)        

print(Asker.kabiliyetler)
        
































    

        