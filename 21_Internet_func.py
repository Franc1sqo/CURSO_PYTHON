# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:59:33 2020

@author: panch1t0
"""

import re
def findInternet(frase):
    if re.findall('internet',frase,re.IGNORECASE):
        print('True')
    else:
        print('False')
frase=input('frase: ')
findInternet(frase)