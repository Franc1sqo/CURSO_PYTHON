# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:33:46 2020

@author: panch1t0
"""

import pandas as pd
titulos=pd.read_csv('data/titles.csv')
print(titulos.head())
print("\n"*2)
elenco=pd.read_csv('data/cast.csv',encoding='utf-8')
print(elenco.head(10))
#cuantas peliculas estan listadas en el dataframe titulos?
print(len(titulos))
# Cual fue la primer pelicula hecha titulada "Romeo and Juliet" ?
print(titulos[titulos.title == "Romeo and Juliet"].sort_values('year').head(1))
# Listar todas las peliculas que contengan la palabra "Exorcist"
# ordenadas de la mas vieja a la mas reciente.
print(titulos[titulos.title.str.contains("Exorcist")].sort_values('year'))
# Cuantas peliculas fueron hechas en el año 1970?
print(len( titulos[titulos.year == 1970] ))
print(len( titulos[titulos.title == "Romeo and Juliet"] ))
# Cuantas peliculas fueron hechas de 1950 a 1959
print(len( titulos[ (titulos.year >= 1950) & (titulos.year <= 1959) ] ))
print(len( titulos[ titulos.year // 10 == 195] ))
# En que años alguna pelicula llamada "Batman" se presento
print(titulos[ titulos.title == "Batman"])
#primera peilcula en 1983
print(titulos[ titulos.year == 1983])
print(len(titulos[ titulos.year == 1983]))
#The godfather#
print(elenco[ elenco.title == "The Godfather"].sort_values('character').head(1))

