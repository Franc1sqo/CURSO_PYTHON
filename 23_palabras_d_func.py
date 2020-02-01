# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:53:29 2020

@author: panch1t0
"""

def palabra(letrad):
# Comprobamos si un numero es múltiple de cinco
    if letrad [0] == 'd' or letrad [0]=='D':
    # Sólo devolvemos True si lo es
        print('True')
        return True
        
seq = ['data','salt' ,'dairy','cat', 'dog']
filter(palabra,seq)

def multiple(numero):
# Comprobamos si un numero es múltiple de cinco
    if numero % 5 == 0:
    # Sólo devolvemos True si lo es
        return True
numeros = [2, 5, 10, 23, 50, 33]
filter(multiple, numeros)