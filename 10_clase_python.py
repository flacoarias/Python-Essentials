# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:56:30 2023

@author: jarias
"""

lista=["R1", "R2", "R3", "S1", "S2", "S3"]
lista2=[]
"""print(len(lista))
print(lista[0])
print(lista[5])

for item in lista:
    #print(item)
    print(item,end=" * ")
"""
"""
for item in lista:
    if "R" in item:
        print(item,end=" * ")"""

for item in lista:
    if "R" in item:
        lista2.append(item)
        #print(item,end=" * ")

print(lista2)