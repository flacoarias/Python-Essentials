# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:35:26 2023

@author: jarias
"""

x=int()
x=5
str1="Cisco"
str2="Networking"
str3="Academy"
space=" "
print(str1,str2,str3, x)
print(str1+space+str2+space+str3+space)
print("El valor de X es: " + str(x))
print(type(x))
x=str(x)
print(type(x))

print(str1+str2+str3)
print(str1,str2,str3)
print(str1,str2,str3, x)


pi=22/7
print(pi)
print("{:.2f}".format(pi))
print("{:.10f}".format(pi))
print("{:.50f}".format(pi))
print("{:.52f}".format(pi))