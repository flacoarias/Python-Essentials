# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:19:08 2023

@author: jarias
"""

datos=200
nativa=100

if datos==nativa:
    print("Las VLAN son iguales")
else:
    if datos>nativa:
        print("Las VLAN son mayores")
    else:
        print("Las VLAN son diferentes")