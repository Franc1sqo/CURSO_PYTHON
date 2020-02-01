# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:18:53 2020

@author: panch1t0
"""

try:
    print("1")
    x=1/0
    print("2")
except:
    print("oh dear, something went wrong")
print("3")

try:
    x=int(input("Enter a number:"))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("no puede dividir para cero, lo siento")
except ValueError:
    print("debe ingresar un valor entero")
except:
    print("ohhh, algo fue mal")
print("end")    

try:
    y=1/0
except ArithmeticError:
    print("Aritmetica problema")
except ZeroDivisionError:
    print("Zero divisio")
print("fin")

