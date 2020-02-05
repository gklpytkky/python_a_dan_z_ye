# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:35:01 2020

@author: Klinik_Muh
"""

kullanicilar = {"volkan" : "qwertyuıopğü",
                "ahmet" : "0123456789"}

isimler = kullanicilar.keys()
kull_adi = input("Kullanıcı Adınız : ")

if kull_adi in isimler:
    print("Hoş geldiniz {}".format(kull_adi))
    parola = input("parolanız : ")
    if parola == kullanicilar[kull_adi]:
        print("sisteme giriş yapıldı!")
    else:
        print("parola hatalı")
else:
    print("böyle bir kullanıcı yok")
