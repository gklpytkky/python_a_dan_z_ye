import random
import os

class Dusman():
    def __init__(self):
        self.sagmi = True
        self.saglik = random.randint(30,70)
        self.kalkan = random.randint(0,10)
        self.guc = random.randint(20,50)

    def vur(self,player):
        damage = self.guc - player.kalkan
        player.saglik -= damage 
        if player.saglik <= 0:
            player.sagmi = False





class Player():
    def __init__(self):
        self.sagmi = True
        self.saglik = 500
        self.kalkan = 20
        self.guc = 55
    
    def vur(self,dusman):
        damage = self.guc - dusman.kalkan
        dusman.saglik -= damage
        if dusman.saglik <= 0:
            dusman.sagmi = False
            dusmanlar.remove(dusman)
            
 
dusmanlar = list()
for i in range(10):
    dusmanlar.append(Dusman())

player = Player()

       
while True:
    os.system("cls")
    print("player durumu --->>> Sağlik: {} ---- Güç:{} ---- Kalkan: {}".format(player.saglik,player.guc,player.kalkan))
    if player.sagmi == False:
        print("game over:")
        quit()
    
    
    if not dusmanlar:
        print("tebrikler")
        quit()
        
    for i in dusmanlar:
        print("{}. Düşman Durum --->>> Sağlik:{} ---- Güç:{} ---- Kalkan:{}".format(dusmanlar.index(i),i.saglik,i.guc,i.kalkan))
    
    secim = int(input("düsman secin:"))
    dusman = dusmanlar[secim]
    player.vur(dusman)
    
    if dusmanlar:
        saldiran = dusmanlar[random.randint(0,len(dusmanlar) -1)]
        saldiran.vur(player)
    
    
    
    
    
    
    
    
    
    
    