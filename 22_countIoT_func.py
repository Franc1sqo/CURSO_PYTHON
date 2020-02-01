# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:22:05 2020

@author: panch1t0
"""

#countIoT
import re
def countIoT(st):
    print(len(re.findall('idt', frase, re.IGNORECASE)))
frase=input('frase: ')
countIoT(frase)