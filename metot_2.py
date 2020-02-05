
"""
abs()        ------> Mutlak deger olarak döndürür
divmod()     ------> Bölüm ve kalanı verir
max()        ------> Maximum değeri bulur
min()        ------> Minimum değer bulunur
sum()        ------> Dizi içindeki tüm sayıları toplar

"""

#%% abs()
print(abs(-2))

#%% divmod()

print(divmod(39,12))

#%% max()

liste = [1,2,3,4,5,6,7,8]

print(max(liste))

#%% max() string

liste = ["volkan","murat","barkın","sevgi","gıyasettin"]

print(max(liste,key=len))

#%% min()

liste = [1,2,3,4,5,6,7,8]

print(min(liste))

#%% min() string

liste = ["volkan","murat","barkın","sevgi","gıyasettin"]

print(min(liste,key=len))

#%% sum()

liste = [1,2,3,4,5]

print(sum(liste))
#%% sum()

liste = [1,2,3,4,5]

print(sum(liste,5))