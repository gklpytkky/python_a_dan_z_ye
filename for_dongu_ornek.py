# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:23:04 2020

@author: Klini
"""

degisken = "asdasdasdasd"

sayi = 0

for i in degisken:
    sayi += 1

print(sayi)

#%%

for sayi in range(0, 100):
    print(sayi,end = " ")
    
#%%
    
for sayi in range(0, 100, 15):
#    print("Bu", str(sayi) + ". dongu")
    print(sayi)