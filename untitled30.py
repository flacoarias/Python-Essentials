# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:58:27 2023

@author: jarias
"""


    
def isYearLeap(year):
    
    if year % 4 != 0: #no divisible entre 4
    	print("No es bisiesto")
    else:
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
     	print("Es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
     	print("No es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
    	print("Es bisiesto")
 

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    # if result == testResults[i]:
    #     print("OK")
    # else:
    #     print("Failed")