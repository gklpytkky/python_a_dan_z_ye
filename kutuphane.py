import os
kitapListe = list()

kitap = ("İnce Memed","Yaşar Kemal")

menu = """
[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[q] Çıkış

"""

def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Ekleme işlemi tamamlandı...")
    print("Ana menüye girmek için enter'a basın!")
    input()


def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    
    else: 
        return False

def kitapCikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        #kitap çıkartılıyor
        liste.remove(kitap)
        print("Kitap çıkartma işlemi tamamlandı")
        print("Ana menüye girmek için enter'a basın!")
        input()
    else:
        print("Arattığınız kitap mevcut değildir.")
        print("Ana menüye dönmek için enter'a basın!")
        input()
        
def listele(liste:list):
    for i in liste:
        print("Kitap Adı : {}    ------->>>>>>>> Yazar: {}".format(i[0],i[1]))
    
    print("Ana menüye dönmek için enter'a basın!")
    input()



while True:
    os.system("cls") #windows için "cls" #linux için "clear" --->>> Terminal ekranını temizler.
    print(menu)
    
    secim = input("işleminizi Seçiniz: ")
    
    if secim == "1":
        kitap_isim = input("Kitabın Adı: ")
        kitap_yazar = input("Yazarın Adı: ")
        kitap = (kitap_isim,kitap_yazar)
        kitapEkle(kitap,kitapListe) #kitap ekleniyor.
        
        
    elif secim == "2":
        kitap_isim = input("Kitabın Adı: ")
        kitap_yazar = input("Yazarın Adı: ")
        kitap = (kitap_isim,kitap_yazar)
        kitapCikar(kitap,kitapListe)
        
        
    elif secim == "3":
        listele(kitapListe)
        
        
        
    elif secim == "q" or secim == "Q":
        print("keyifli okumalar...")
        quit()
    
    else:
        print("hatalı giriş yaptınız.")
        
