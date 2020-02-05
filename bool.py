"""

and
or
not

"""

#%%
sayi = int(input("sayi gir: "))

if sayi > 5 and sayi % 2 == 0:
        print("dogru")
        
#%%
sayi = int(input("sayi gir: "))

if sayi >= 5:
        print("dogru")
        
#%%    
sayi = int(input("sayi gir: "))

if sayi > 5 or sayi == 5:
        print("dogru") 

#%%
x = int(input("x gir: "))
y = int(input("y gir: "))        

if x == 5 or y == 5:
    print("dogru")
else:
    print("en az birisi 5 olmak zorunda")
    
#%%

x = input("x gir: ")
y = input("y gir: ")       
    
if not bool(x):
    print("dogru")