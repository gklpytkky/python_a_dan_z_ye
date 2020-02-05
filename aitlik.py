## in işleci

#%%

x = "abc"
 
if "b" in x:
     print("mevcut")

#%%

x = "abc"
 
if "e" in x:
     print("mevcut")

#%%

x = "abcdefg"

if "a" not in x:
    print("A harfi yok")

else:
    print("A harfi var")

#%%

x = "bcdefg"

if "a" not in x:
    print("A harfi yok")

else:
    print("A harfi var")    

#%%

giris = input("parola belirle : ")

if "_" not in giris:
    print(" '_' (alt cizgi) kullanmalısınız")

else:
    print("parola belirleme basarılı")    