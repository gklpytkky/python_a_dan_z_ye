kitapListe = ["ince memed","endgame","efendi","cemo","python","c++"]

for i in kitapListe:
    print("kitap adı: {}".format(i))


eklenecek = input("kitap adı: ")

kitapListe += [eklenecek]

print(kitapListe)
