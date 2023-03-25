# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:48:03 2023

@author: jarias
"""

def fibonnacci(nterms):
    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Ingrese un numero positivo")
    elif nterms == 1:
        print("La secuencia de Fibonacci es",nterms,":")
        print(n1)
    else:
        print("La Secuencia de Fibonacci es:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

def Fibonacci(n):
    a, b = 0,1
    while a <= n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
        #a, b = b, a+b
    print()