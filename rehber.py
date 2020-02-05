rehber = {
    "karakter1" : {"ev adresi" : "kavak caddesi no 14",
                   "is adresi" : "osmangazia mahallesi 21 sokak no 15",
                   "ev telefonu" : "506521351",
                   "iş telefonu" : "560510650",
                   "cep telefonu" : "12324165"}
}

isimler = rehber.keys()

arananKisi = input("Aranan isim: ")

if arananKisi in isimler:
    flag = True
else:
    flag = False
    
arananOzellik = input("Aranan Bilgi: ")

if flag:
    print(rehber.get(arananKisi).get(arananOzellik,"bilgi bulunamadı"))
else:
    print("aranan kişi rehberde bulunamadı")