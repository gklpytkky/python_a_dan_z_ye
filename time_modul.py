import time

for i in dir(time):
    if "__" not in i:
        print(i)

#%%

zaman1 = time.time()
time.sleep(2)
zaman2 = time.time()        

print("fark: {}".format(zaman2-zaman1))

