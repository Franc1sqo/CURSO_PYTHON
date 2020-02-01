# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:27:47 2020

@author: panch1t0
"""
def GetDomain(domain):
    c=domain.index('@')
    print(domain[c:])
dominio=input('Ingrese dominio ')
GetDomain(dominio)