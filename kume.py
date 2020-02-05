"""
metotlar:
    
    ----->>> öğe ekle       add
    ----->>> fark           difference
    ----->>> öğe sil        discard
    ----->>> öğe sil        remove
    ----->>> kesişim        intersection

"""
    
string = "asdasdasdqw"
kume = set(string)

print(kume)

#%%
kume = {"deneme","deneme2","deneme3",12,56}

print(type(kume))

#%%

kume = set([1,2,3,4,5])

for i in dir(kume):
    if "__" not in i:
        print(i)

#%%

kume = set([1,2,3,4,5])

kume.add("deneme")

print(kume)
#%%
kume = set([1,2,3,4,5])

kume.discard(3)

print(kume)

#%%
kume = set([1,2,4,5])

kume.remove(3)

print(kume)

#%%
a = set([1,2,4,5])
b = set([2,4,5,6,7,8])

print(a)
print(b)

print(25*"=")

print(a.difference(b))

#%%
print(b.difference(a))

#%%
b.difference_update(a)

print(b)
print(a)

#%%
a = set([1,2,4,5])
b = set([2,4,5,6,7,8])

print(a)
print(b)

print(25*"=")

print(b.intersection(a))



