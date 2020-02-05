# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:41:49 2020

@author: Klinik_Muh
"""

bolunen = float(input("bölünen:"))

bolen = float(input("bölen:"))

print("sonuc :",bolunen/bolen)

#%%

bolunen = float(input("bölünen:"))

bolen = float(input("bölen:"))

try:
    print("sonuc: ",bolunen/bolen)

except ZeroDivisionError:
    print("0 a bölüm tanımsızdır")

#%%

bolunen = float(input("bölünen:"))

bolen = (input("bölen:"))

try:
    print("sonuc: ",bolunen/bolen)

except ZeroDivisionError:
    print("0 a bölüm tanımsızdır")    
    
except TypeError:
    print("veri tipi desteklenmiyor")
    
#%%

bolunen = float(input("bölünen:"))

bolen = float(input("bölen:"))

try:
    print("sonuc: ",bolunen/bolen)

except ZeroDivisionError as hata:
    print("0 a bölüm tanımsızdır")   
    print("gerçek hata:")
    print(hata)
    
except TypeError:
    print("veri tipi desteklenmiyor")

#%%

bolunen = float(input("bölünen:"))

bolen = float(input("bölen:"))

try:
    print("sonuc: ",bolunen/bolen)

except ZeroDivisionError as hata:
    print("0 a bölüm tanımsızdır")   
    print("gerçek hata:")
    print(hata)
    
except TypeError:
    print("veri tipi desteklenmiyor")
    
finally:
    print("Bu hep var")        
    
#%%

bolunen = float(input("bölünen:"))

bolen = float(input("bölen:"))

try:
    print("sonuc: ",bolunen/bolen)

except:
    print("hata oluştu")

    
finally:
    print("Bu hep var")       
    
    
    
    
    
    
    
    
    
    
    
