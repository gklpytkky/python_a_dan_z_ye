# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:46:03 2020

@author: Klini
"""

def sagSlah(adet):
    for i in range(int(adet)):
        print("/",end="")
        
def solSlah(adet):
   for i in range(int(adet)):
       print("\\",end="")

def satirAtla(adet):
    for i in range(int(adet)):
        print()
        
def bosluk(adet):
    for i in range(int(adet)):
        print(" ",end="")
        
def ustKisim(cap):
    baslangicBosluk = cap / 2-1
    for i in range(int(cap/2)):
        bosluk(baslangicBosluk-i)
        sagSlah(1)
        bosluk(i*2)
        solSlah(1)
        satirAtla(1)

def altKisim(cap):
    baslangicBosluk = cap-2
    for i in range(int(cap/2)):
        bosluk(i)
        solSlah(1)
        bosluk(baslangicBosluk - i*2)
        sagSlah(1)
        satirAtla(1)
        
def paralelKenar(cap):    
    ustKisim(cap)
    altKisim(cap)
    
paralelKenar(20)
        
