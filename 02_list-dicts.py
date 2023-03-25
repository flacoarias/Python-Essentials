# Create a list of the BRICS countries
country = ["Brazil", "Russia", "India", "China", "South Africa"]

"""Create a dictionary of BRICS capitals. Note that South Africa has 3 capitals. 
   Therefore, we embed a list inside the dictionary."""
capitals = {"Brazil": "Brasilia",
            "Russia": "Moscow",
            "India": "New Delhi",
            "China": "Beijing",
            "South Africa": ["Pretoria", "Cape Town", "Bloemfontein"]}

# Print the list and dictionary
""" What response did you get? Why did the list and dictionary contents not print?
    Fix the code and run the script again. print("country") print( "capitals")
"""
#  El error en la lista country(paises), era porque estaba colocado entre comillas
#  y eso hace que le reconozca como cadena o tipo string, mas no como una lista.
print(type(country))
print("Países: ", country)
print("\n"*1)

#  El error en el diccionario de capitals(capitales), era poque estaba colocado 
#  entre comillas y eso hace que le reconozca como cadena o string, más no como
#  un diccionario.
print(type(capitals))
print("Países y sus Capitales: ", capitals)
print("Capitales: ", capitals.values())
print("\n"*1)

"""Why did you get an error for the 2nd capital of South Africa?
   Hint: Check the syntax for the index value.
   print(capitals["South Africa"[1]])"""
#  El error está en que falta un corchete que cierre en la instrucción de impresión
#  por lo que colocando desaparece el error e imprime la capital Cape Town(Ciudad
#  del Cabo). 
print("South Africa", capitals["South Africa"][1])