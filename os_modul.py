import os

for i in dir(os):
    if "__" not in i:
        print(i)
        
#%%
bulundugum_dizin = os.getcwd()
print(bulundugum_dizin)
print("dizin değişti")

os.chdir("../../")
bulundugum_dizin = os.getcwd()
print(bulundugum_dizin)   

#%%
print("bişeyler bişeyler")
input("bas enter")
os.system("clear")   

#%%  
ev_dizini = os.path.expanduser("~")

print(ev_dizini)
os.chdir(ev_dizini)
print(os.getcwd())

print("dosya ve klasörler")
for i in os.listdir("."):
    print(i)
    
#%%

