# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:22:35 2020

@author: panch1t0
"""
def fib(n):
    anterior=0
    despues=1
    fib=0
    for i in range (1,n+1):
        print(fib)
        fib=anterior+despues
        anterior=despues
        despues=fib
print(fib(5))