dosya = open("deneme.txt","w")

yazilacaklar = "deneme bir yazidir bu+.."

dosya.write(yazilacaklar)

dosya.close

#%%
 
dosya = open("deneme.txt","r")

okunan = dosya.readlines()

print(okunan)

type(okunan)

dosya.close()

#%%
"""

"r" ---->> okuma
"w" ---->> yazma
"a" ---->> yazma
"x" ---->> okuma (varsa hata verir)

"r+" ---->> okuma ve yazma (var olması gerekir)
"w+" ---->> okuma ve yazma (varsa siler)
"a+" ---->> okuma ve yazma  
"x+" ---->> okuma ve yazma

"""
#%%
dosya = open("deneme.txt","a")

dosya.write("\ndeneme satiri 3")

dosya.close()
#%%
#dosya = open("deneme.txt","x")
#
#dosya.write("deneme satiri 4")
#
#dosya.close()
#%%
dosya = open("deneme.txt","r+")

dosya.write("deneme satiri 3")

dosya.close()
#%%
dosya = open("deneme.txt","w+")

dosya.write("deneme satiri 4")

dosya.close()
#%%
dosya = open("deneme.txt","w+")

dosya.read()
dosya.write("deneme satiri 4")

dosya.close()
#%%
dosya = open("deneme.txt","x+")

dosya.read()
dosya.write("deneme satiri 3")

dosya.close()





