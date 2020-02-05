# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:36:12 2020

@author: Klinik_Muh
"""

string = "elma"

newString = string.replace("e","E")

print(newString)

#%%

string = "eeee"

newString = string.replace("e","E")

print(newString)

#%%
string = "İstanbul Büyükşehir Belediyesi"

newList = string.split("l")

print(newList)
#%%
string = "İstanbul Büyükşehir Belediyesi"

newList = string.split("")

print(newList)
#%%
string = "İstanbul Büyükşehir Belediyesi"

newList = string.split(" ",1)

print(newList)
#%%
string = "İstanbul Büyükşehir Belediyesi"

newList = string.rsplit(" ",1)

print(newList)
#%%
string = "İstanbul Büyükşehir Belediyesi"

newString = string.lower()

print(newString)
#%%
string = "İstanbul Büyükşehir Belediyesi"

newString = string.upper()

print(newString)
