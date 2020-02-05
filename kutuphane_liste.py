kitapListesi = list()

menu = """
[1] kitap ekle
[2] kitap cikar
[3] kitapları listele
[Q] cikis

"""

def kitapEkle(kitap,liste):
    liste += [kitap]
    print("kitap eklendi")
    input("ana menüye dönmek için enter")

def kitapCikar():
    pass

def listele(liste):
    for i in liste:
        print("kitap adi {} ".format(i))
    print()
    input("ana menüye dönmek için enter")

def cik():
    quit()

while True:
    print(menu)

    secim = input("seciminiz: ")

    if secim == "1":
        kitapAdi = input("kitap adi: ")
        kitapEkle(kitapAdi,kitapListesi)
        
    elif secim == "2":
         kitapCikar()
        
    elif secim == "3":
         listele(kitapListesi)
    
    elif secim == "q" or secim == "Q":
         print("cikis yapılıyor")
         cik()
        
    else:
        print("hatalı girdiniz")
        input("ana menüye dönmek için enter")
        

            
         
