# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:17:55 2020

@author: panch1t0
"""

file=open("devices.txt","r")
for item in file:
    print(item)
file.close()

devices=[]
file=open("devices.txt","r")
for item in file:
    item = item.strip()
    devices.append(item)
file.close()
print (devices)