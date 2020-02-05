# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:11:56 2020

@author: Klinik_Muh
"""

for i in dir(dict()):
    if "__" not in i:
        print(i)
        
#%%

sozluk = {"book":"kitap","computer":"bilgisayar","mobile":"telefon","pen":"kalem"}

s = input("Sogru: ")

print(sozluk[s])

#%%

sozluk = {"book":"kitap","computer":"bilgisayar","mobile":"telefon","pen":"kalem"}

s = input("Sogru: ")

print(sozluk.get(s,"aratılan kelime bulunamadı"))

#%%
sozluk = {"book":"kitap","computer":"bilgisayar","mobile":"telefon","pen":"kalem"}

for i in sozluk.items():
    print(i)

#%%

sozluk = {"book":"kitap","computer":"bilgisayar","mobile":"telefon","pen":"kalem"}

for i in sozluk.keys():
    print(i)  

for i in sozluk.values():
    print(i)
    
#%%
sozluk = {"book":"kitap","computer":"bilgisayar","mobile":"telefon","pen":"kalem"}

sozluk2 = sozluk.copy()

print(sozluk2)
    
