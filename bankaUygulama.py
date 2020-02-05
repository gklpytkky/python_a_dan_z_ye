from os import system as komut 

class Musteri():
    def __init__(self,ID,PAROLA,ISIM):
        self.isim = ISIM
        self.id = ID
        self.parola = PAROLA
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler = list()
    
    def musteri_ol(self,ID:str,PAROLA:str,ISIM:str):
        self.musteriler.append(Musteri(ID,PAROLA,ISIM))
        print("Bankamıza kayıt yaptırdığınız için teşekkürler")

def main():
    banka = Banka()
    while True:
        komut("cls")
        print("""
        [1] Banka Müşterisiyim
        [2] Banka Müşterisi Olmak İstiyorum
        """)
        
        secim = input("Seciminiz: ")
        
        if secim == "1":
            ids = [i.id for i in banka.musteriler]
            ID = input("ID: ")
            if ID in ids:
                for musteri in banka.musteriler:
                    if ID == musteri.id: #müsteri bulundu
                        print("Hoşgeldiniz {}".format(musteri.isim))
                        parola = input("parolanız: ")
                        if parola == musteri.parola:
                            print("Giriş Başarılı")
                            while True:
                                komut("cls")
                                print("""
                                [1] Bakiye Sorgulama
                                [2] Para Yatır (Kendi Hesabıma)
                                [3] Para Yatır (Baskasının Hesabına)
                                [4] Para Çek
                                [q] Çıkış
                                """)
                                
                                secim2 = input("İşleminiz: ")
                                
                                if secim2 == "1":
                                    print("Bakiyeniz: {}".format(musteri.bakiye))
                                    input("Ana menuüye dönmek için ENTER a basın")
                                
                                elif secim2 == "2":
                                    miktar = int(input("Miktar: "))
                                    onay = input("Kendi hesabınıza {} TL para yatırma işlemini onaylıyormusunuz: E/H\n".format(miktar))
                                    if onay == "E" or onay == "e":
                                        musteri.bakiye += miktar
                                        print("Paranız yatırıldı")
                                        input("Ana menüye dönmek için ENTER a basın")
                                    
                                    elif onay == "h" or onay == "H":
                                        print("İşlem iptal edildi")
                                        input("Ana menüye dönmek için ENTER a basın")
                                
                                    else:
                                        print("Hatalı girildi işlem iptal")
                                        input("Ana menüye dönmek için ENTER a basın")
                                        
                                elif secim2 == "3":
                                    arananID = input("Müsteri ID: ")
                                    if arananID in ids:
                                        for digerMusteri in banka.musteriler:
                                            if arananID == digerMusteri.id:
                                                miktar = int(input("Miktar: "))
                                                if miktar <= musteri.bakiye:
                                                    onay = input("{} adlı müsterimize {} TL para atırma işlemini onaylıyormusunuz: E/H\n".format(digerMusteri.isim,miktar))
                                                    if onay =="e" or onay =="E":
                                                        digerMusteri.bakiye += miktar
                                                        musteri.bakiye -= miktar
                                                        print("Para aktarıldı")
                                                        input("Ana menüye dönmek için ENTER a basın")
                                                    
                                                    elif onay =="h" or onay == "H":
                                                        print("işlem iptal edildi.")
                                                        input("Ana menüye dönmek için ENTER a basın")
                                                
                                                    else:
                                                        print("Hatalı giriş işlem iptal")
                                                        input("Ana menüye dönmek için ENTER a basın")
                                                
                                                else:
                                                    print("Bakiyeniz bu işlem için yetersiz")
                                                    input("ana menüye dönmek için ENTER a basınız")
                                            
                                    else:
                                        print("Müsteri bulunamadı")
                                        input("ana menüye dönmek için ENTER a basınız")
                                                
                                elif secim2 == "4":
                                    miktar = int(input("Miktar: "))
                                    if miktar <= musteri.bakiye:
                                        musteri.bakiye -= miktar
                                        print("işlem tamamlandı, paranızı alınız")
                                        input("ana menüye dönmek için ENTER a basınız")
                                    else:
                                        print("bakiyeniz bu işlem için yetersiz")
                                        input("ana menüye dönmek için ENTER a basınız")
                                
                                elif secim2 == "q" or secim2 == "Q":
                                     break  
    
    

        elif secim == "2":
            ID = input("ID: ")
            ISIM = input("isminiz: ")
            PAROLA = input("parola: ")
            banka.musteri_ol(ID,PAROLA,ISIM)
            
            



if __name__ == "__main__":
   main()
                                        
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                    
                                    
                                    