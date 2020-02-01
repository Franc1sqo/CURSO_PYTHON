# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:29:17 2020

@author: panch1t0
"""
import re
file=open("devices.txt","a")
while True:
    newitem=str(input('nuevo device:'))
    if re.findall('exit',newitem,re.IGNORECASE):
        print('all done')
        break
    else:
        file.write(newitem + "\n")
file.close()