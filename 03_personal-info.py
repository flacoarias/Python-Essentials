# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:31:03 2023

@author: jarias
"""

"""first_name = input("Ingrese sus Nombres: ")
last_name = input("Ingrese sus Aellidos: ")
location = input("Ingrese su Ubicación: ")"""
#age = int(input("Ingrese su Edad: "))
#space = " "
"""print("Estimado: ", first_name, space, last_name, space, ", de parte de la PUCESI, le")
print("damos la bienvenida, nos complace conocer que usted es de: ", location)
print("y que su edad actual es: ", age, space, ", queremos darle a conocer nuestra ")
print("amplia oferta académica tanto en carreras Técnicas, como de Grado y Postgrado.")
print("es un placer recibirlo en nuestro campus universitario.")"""

age = int(input("Ingrese su Edad: "))
if age >= 0 and age <=5:
    print("Primera Infancia")
elif age >= 6 and age <=11:
    print("Infancia")
elif age >= 12 and age <=18:
    print("Adolescencia")
elif age >= 18 and age <=26:
    print("Jóvenes")
elif age >= 27 and age <=59:
    print("Adulto")
elif age >= 60:
    print("Vejez")
else:
    print("No ha nacido")