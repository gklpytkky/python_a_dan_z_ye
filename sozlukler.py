sozluk = {"home" : "ev" , 
          "book" : "kitap",
           "pen" : "kalem"}

print(sozluk["home"])
print(sozluk["book"])
print(sozluk["pen"])

#%%

karakter = {"ad" : "volkan",
            "guc" : 100,
            "silah" : "kilic",
            "can":100}

print("karakterin adı    : {}".format(karakter["ad"]))
print("karakterin gücü   : {}".format(karakter["guc"]))
print("karakterin silahı : {}".format(karakter["silah"]))

karakter2 = {"ad":"karakter2",
             "guc":70,
             "silah":"kilic",
             "can":100}

def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["guc"]
    vurulan["can"] = vurulan["can"] - eksilen
    
vur(karakter,karakter2)
vur(karakter2,karakter)

print("karakter 1 can : ",karakter["can"])
print("karakter 2 can : ",karakter2["can"])
