
print("""
      
[1] Toplama islemi
[2] Cikarma islemi
[3] Carpma islemi
[4] Bolme islemi
[5] Us alma
[Q] Cikis

      """)


giris = input("Seciminiz: ")

if giris == "1":
    x = input("ilk sayi: ")
    x = float(x)
    y = input("ikinci sayi: ")
    y = float(y)
    
    print("======================")
    print("islem sonucu: ", x + y) ## toplama i�lemi 
    print("======================")

elif giris == "2":
    x = input("ilk sayi: ")
    x = float(x)
    y = input("ikinci sayi: ")
    y = float(y)
    
    print("======================")
    print("islem sonucu: ", x - y) ## ��karma i�lemi 
    print("======================")
    
elif giris == "3":
    x = input("ilk sayi: ")
    x = float(x)
    y = input("ikinci sayi: ")
    y = float(y)
    
    print("======================")
    print("islem sonucu: ", x * y) ##�arpma i�lemi
    print("======================")
    
elif giris == "4":
    x = input("ilk sayi: ")
    x = float(x)
    y = input("ikinci sayi: ")
    y = float(y)
    
    print("======================")
    print("islem sonucu: ", x / y) ## b�lme i�lemi
    print("======================")
    
elif giris == "5":
    x = input("Taban: ")
    x = float(x)
    y = input("Kuvvet: ")
    y = int(y)
    
    print("======================")
    print("islem sonucu: ", x ** y) ##�s alma i�lemi i�in ** kullan�l�n�r. karesi
    print("======================")
    
elif giris == "q" or giris == "Q":
    
    print("======================")
    print("Cikis yapiliyor...")
    print("======================")
    quit() 

else:
    print("======================")
    print("hatali giris")
    print("======================")

