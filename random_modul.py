import random

for i in dir(random):
    if "__" not in i:
        print(i)

#%%
from random import randint
from os import system as komut

komut("cls")

rastgeleSayi = randint(10,50)
print("tutulan sayi",rastgeleSayi)
print("10 ile 50 arasında bir sayı tuttum. Bil bakalım kaç")
tahmin = int(input("tahmin:"))

if tahmin == rastgeleSayi:
    komut("clear")
    print("tebrikler")
else:
    komut("clear")    
    print("bilemediniz")



