"""
   ==     -----> eşitse
   !=     -----> eşit değilse
    >     -----> büyükse
    <     -----> küçükse
   >=     -----> büyük eşitse
   <=     -----> küçük eşitse
   
"""

#%%

giris = input("parola: ")

sifre = "deneme"

if giris != sifre:
    print("parola yanlis")

#%%
    giris = input("10 ile 100 arasinda sayi girin: ")
    
    giris = int(giris)
    
    
    if giris > 50:
        print("50 den büyük")
    elif giris < 50:
        print("50 den küçük")
    else:
        print("sayı 50")

#%%

    giris = input("10 ile 100 arasinda sayi girin: ")
    
    giris = int(giris)
    
    if giris >= 50:
        print("50 den büyük veya 50'ye eş")
    elif giris < 50:
        print("50'den küçük")

#%%

    giris = input("10 ile 100 arasinda sayi girin: ")
    
    giris = int(giris)
    
    if giris > 50:
        print("50 den b�y�k")
    elif giris <= 50:
        print("50'den kucuk veya 50'ye esit")
