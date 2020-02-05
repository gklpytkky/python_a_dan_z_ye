# import sqlite3


# veriler = [
#     ("Ahmet Ümit","İstanbul Hatırası"),
#     ("Yaşar Kemal","İnce Memed"),
#     ("Paulo Coelho","Simyacı"),
#     ("Paulo Coelho","Aldatma")]


# db = sqlite3.connect("kitaplar.sqlite")

# imlec = db.cursor()

# imlec.execute("CREATE TABLE IF NOT EXISTS 'kitaplik tablosu' (yazar,kitap)")

# for veri in veriler:
#     imlec.execute("INSERT INTO 'kitaplik tablosu' VALUES (?,?)",veri)




# db.commit()
# db.close()

#%%
# import sqlite3

# db = sqlite3.connect("kitaplar.sqlite")
# imlec = db.cursor()

# imlec.execute("SELECT * FROM 'kitaplik tablosu'")

# veriler = imlec.fetchall()
# for veri in veriler: 
#     print(veri)

# db.close()

#%%

# import sqlite3

# db = sqlite3.connect("kitaplar.sqlite")
# imlec = db.cursor()

# imlec.execute("SELECT * FROM 'kitaplik tablosu'")

# print(imlec.fetchone())
# print(imlec.fetchone())
# print(imlec.fetchone())
# print(imlec.fetchone())

# db.close()

#%%

# import sqlite3

# db = sqlite3.connect("kitaplar.sqlite")
# imlec = db.cursor()

# imlec.execute("SELECT * FROM 'kitaplik tablosu'")

# veriler = imlec.fetchmany(5)

# for i in veriler:
#     print(i)

# db.close()

#%%

# import sqlite3

# db = sqlite3.connect("kitaplar.sqlite")
# imlec = db.cursor()

# # imlec.execute("SELECT * FROM 'kitaplik tablosu' WHERE yazar = 'Paulo Coelho'")
# imlec.execute("SELECT * FROM 'kitaplik tablosu' WHERE yazar = 'Ahmet Ümit'")

# veriler = imlec.fetchall()

# for i in veriler:
#     print(i)

# db.close()

#%%

import sqlite3

db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

menu = """
[1] Kitap Ara
[2] Yazar Ara

"""

print(menu)

islem = input("İşleminiz: ")

if islem == "1":
    isim = input("Kitap Adı: ")
    sorgu = "SELECT * FROM 'kitaplik tablosu' WHERE kitap = '{}'".format(isim)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)

if islem == "2":
    isim = input("Yazar Adı: ")
    sorgu = "SELECT * FROM 'kitaplik tablosu' WHERE kitap = '{}'".format(isim)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)        



db.close()


