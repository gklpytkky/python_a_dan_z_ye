# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:40:01 2020

@author: Klini
"""

#x = 5 değişken
# def fonksiyon

def topla():
    sonuc = 3 + 5
    print(sonuc)
    
topla()
print("selam")
topla()
topla()

#%%

def topla(birinciSayi,ikinciSayi):
    sonuc = birinciSayi + ikinciSayi
    print(sonuc)

topla(3,9)
topla(2,8)
topla(1,234)

#%%
def topla(birinciSayi,ikinciSayi):
    sonuc = birinciSayi + ikinciSayi
    return(sonuc)

print(topla(3,5))

print("burada aslinda sayi var : ",topla(12,23))

