            #0      #1         #2          #3      #4
liste = ["volkan","tasci","123123123","987987987",65.4,["asdasdasd",12,34.6,"ceyda"]]

print(liste[1])

print(liste[-1])

print(liste[-1][2])

print(liste[0][2])

#%%
kelime = "volkan"

print(kelime[2])

#%%
            #0      #1         #2          #3      #4      #0       #1  #2     #3       #4
liste = ["volkan","tasci","123123123","987987987",65.4,["asdasdasd",12,34.6,["a","b"],"ceyda"]]
                                                                             #0  #1
                                                        #(              -1                    )
print(liste[-1][3][1])                                                        
