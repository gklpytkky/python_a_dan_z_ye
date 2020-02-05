cumle = """
English: Hello World
Turkce : {} {}
""".format("Merhaba","Dunya")

print(cumle)

#%%
karakterler = "abcdefg"

for i in karakterler:
    print("bastırılan karakter: {}".format(i))
#%%
char = "123456789"

for i in char:
    print("bastirilan karakter: ",(i))
#%%
    
degisken1 = "volkan"
degisken2 = "tasci"

ifade1 = "{0} {1}".format(degisken1,degisken2)
ifade2 = "{1} {0}".format(degisken2,degisken1)

print(ifade1)
print(ifade2)

#%%

degisken1 = "volkan"
degisken2 = "tasci"

ifade1 = "{ad} {soyad}".format(soyad = degisken2,ad = degisken1)
ifade2 = "{1} {0}".format(degisken2,degisken1)

print(ifade1)
print(ifade2)

#%%
degisken1 = "volkan"
degisken2 = "tasci"

ifade1 = "|{:>15}|".format(degisken1)
ifade2 = "{1} {0}".format(degisken2,degisken1)

print(ifade1)
print(ifade2)

#%%
degisken1 = "volkan"
degisken2 = "tasci"

ifade1 = "|{:^15}|".format(degisken1)
ifade2 = "{1} {0}".format(degisken2,degisken1)

print(ifade1)
print(ifade2)

#%%
degisken1 = "volkan"
degisken2 = "tasci"

ifade1 = "|{:b}|".format(1024)
ifade2 = "{}".format(12)

print(ifade1)
print(ifade2)




