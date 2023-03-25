# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:56:40 2023

@author: jarias
"""

#Lista de Listas
lista=["1",2,3.5,True,"1"]
print(type(lista))
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[-1])
print(lista[-5])
#print(lista[5]) no existe la posición 5
#print(lista[-6]) no existe la posición -5
lista[4]="4"
print(lista[4])
del lista[4]

#Lista de tuplas
tupla=("1",2,3.5,True,"1")
print(type(tupla))
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])
print(tupla[4])
#tupla[4]="4" no soporta la asignacion en la tupla
#del tupla[4] no soporta el borrado en la tupla