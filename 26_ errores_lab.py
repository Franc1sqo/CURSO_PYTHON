# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:50:47 2020

@author: CEC
"""

def readint(prompt, min, max):
#
# put your code here
    while (True):
        try:
            x=int(input())
            assert x >= min and x <= max
            return x
            break
        except ValueError:
            print("Error: wrong input")
            return None
        except:
            print("El valor debe estar dentro del RANGO --> (-10..10) <--")
    
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)


def validarNumero(prompt, min, max):
    while (True):
        try:
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
            break
        except ValueError:
            print("Ingresar solo numeros")
        except:
            print("El valor debe estar dentro del RANGO --> (-10..10) <--")
    
v = validarNumero("Ingrese un valor desde -10 a 10:", -10, 10)

print("El número es:", v)