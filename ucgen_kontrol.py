# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:51:49 2020

@author: Klini
"""
#%%
def ucgenmi(a,b,hipo):
    if a**2 + b**2 == hipo**2:
        return "bu bir ucgendir!"
    else:
        return "bu bir ucgen degildir!"

print(ucgenmi(2,5,7))

print(ucgenmi(3,4,5))
