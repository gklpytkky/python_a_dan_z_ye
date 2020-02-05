#integer sayıların metotları

"""
bit_length()       -------> bit uzunluğu
"""

#float sayılaın metotları

"""
as_integer_ratio()  -------> bölüm sonucu çıkması için gereken tam sayıları verir

is_integer()        -------> sayı tam sayı ise True döndürür

"""

#karmaşık sayıların metotları

"""
imag               -------> complex sayıların sanal kısmını verir

real               -------> complex sayıların gerçek kısmını verir

"""

sayi = 5
print(sayi.bit_length())

#%%
sayi = 4.5

print(sayi.as_integer_ratio())

#%%
sayi = 4.0
print(type(sayi))
print(sayi.is_integer())

#%%
karmasik = 12+4j

print("gerçek kısım: ",(karmasik.real))
print("sanal kısım: ",karmasik.imag)
