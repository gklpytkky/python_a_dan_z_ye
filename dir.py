liste = ["deneme1","deneme2"]

print(liste)

liste += ["deneme3"]

print(liste)

#%%

liste = ["deneme1","deneme2"]

#print(dir(liste))

for i in dir(liste):
    print(i)
#%%

liste.append("deneme3")

liste.remove("deneme1")

print(liste)    

string = ""

for i in dir(string):
    print(i)
