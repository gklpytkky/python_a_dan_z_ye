# is işleci 
# id fonksiyonu

#%%
a = 5
b = 5

if a == b:
    print("ayni")

if a is b:
    print("ayni")
    
#%%
    
a = 5
b = 5

print(id(a))
print(id(b))
print(id(5))

#%%

a = 5
b = 5

if a is b:
    print("ayni")
    
# is işleci id kontrolü yapmak 
# == işleci eşitlik kontrolü yapmak 
