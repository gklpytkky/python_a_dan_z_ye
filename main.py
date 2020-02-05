
kitap = ("ahmer ümit","istanbul hatırası",300)

print("yazar: {}".format(kitap[0]))
print("kitap adı: {}".format(kitap[1]))
print("kitap sayfa sayısı: {}".format(kitap[2]))

#%%
kutuphane = []


kitap1 = ("ahmer ümit","istanbul hatırası",300)

kutuphane.append(kitap1)

print(kutuphane[0])
 #%%
kutuphane = []


kitap1 = ("ahmer ümit","istanbul hatırası",300)

kutuphane.append(kitap1)

kutuphane.remove(kitap1)

print(kutuphane[0])

#%%
kutuphane = []


kitap1 = ("ahmer ümit","istanbul hatırası",300)
kitap2 = ("paulo coelho","aldatma",300)

kutuphane.append(kitap1)

print(kutuphane)

def kitapVarmi(hangi_Kitap:tuple):
    if hangi_Kitap in kutuphane:
        return True
    else:
        return False


def kitapCikar(hangi_Kitap:tuple):
   if kitapVarmi(hangi_Kitap):
       kutuphane.remove(hangi_Kitap)
       print("kitap çıkarıldı")
   else:
       print("çıkarılmaya çalışılan kitap mevcut değil")
       
def kitapEkle(hangi_Kitap):
    kutuphane.append
    print("kitap eklendi")

kitapCikar(kitap2)
#kitapCikar(kitap1)

kitapEkle(kitap1)
#kitapEkle(kitap2)

print(kutuphane)
