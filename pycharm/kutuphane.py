kitapListesi = list()

menu = """
[1] Kitap Ekle
[2] Kitap Cikar
[3] Kitaplari Listele
[Q] Cikis

"""


def kitapEkle(kitap, liste):
    liste += [kitap]
    print("kitap eklendi")
    input("ana menuye donmek icin ENTER basin")


def kitapCikar():
    pass


def listele(liste):
    for i in liste:
        print("kitap Adi ------->>>>>>> {} ".format(i))
        print()
        input("ana menuye donmek icin ENTER basin")


def cik():
    quit()


while True:
    print(menu)

    secim = input("seciminiz: ")

    if secim == "1":
        kitapAdi = input("kitap Adı : ")
        kitapEkle(kitapAdi, kitapListesi)

    elif secim == "2":
        kitapCikar()

    elif secim == "3":
        listele(kitapListesi)

    elif secim == "q" or secim == "Q":
        cik()

    else:
        print("hatalı girdiniz")
        input("ana menuye donmek icin ENTER basin")
