for i in dir(list()):
    if "__" not in i:
        print(i)
        
print("===================")
#%%

liste = ["ince memed","simyacı","otomatik portakal","cemo","simyacı"]

liste.append("Ruby")
liste.append("c##")
#liste.remove("simyacı")

def listele(liste):
    for i in liste:
        print(i)

listele(liste)

#%%     

liste = ["ince memed","simyacı","otomatik portakal","cemo","simyacı"]

liste.append("Ruby")
liste.append("c##")
#liste.remove("simyacı")

def listele(liste):
    for i in liste:
        print(i)

print(liste.count("simyacı"))

print(liste.count("ince memed"))

#%%

liste = ["ince memed","simyacı","otomatik portakal","cemo","simyacı"]

liste.append("Ruby")
liste.append("c##")
#liste.remove("simyacı")

def listele(liste):
    for i in liste:
        print(i)    

print(liste.count("ince memed"))

liste2 = liste.copy()

print("durum1:")
print(liste)
print(liste2)
print(30*"=")

liste.remove("ince memed")
liste.remove("simyacı")
liste.append("bla bla bla")
liste2.append("volkan")
liste2.extend(liste)

print("durum2:")        
print(liste)
print(liste2)
print(30*"=")

#%%

def listele(liste):
    for i in liste:
        print(i)   
        
liste = ["ince memed","simyacı","otomatik portakal","cemo","simyacı"]

sira = liste.index("otomatik portakal")
print(sira)

#%%

def listele(liste):
    for i in liste:
        print(i)   
        
#liste = ["ince memed","simyacı","otomatik portakal","cemo","simyacı"]

liste = [3,5,7,1,0,5,7,19] 

print(liste)

liste.sort()

print(liste)

#%%

for i in dir(tuple()):
    if "__" not in i:
        print(i)

#%%
demet = ("deneme1","deneme2","volkan","volkan")

count = demet.count("volkan")

index = demet.index("volkan")

print(count)
print(index)

#%%














