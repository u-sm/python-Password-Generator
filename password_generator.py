# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 15:56:54 2023

@author: admin
"""

# Strong password generator

import random

# Funtion to shuffle the characters

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Main program starts here

uppercaseletter1 = chr(random.randint(65,90))

lowercaseletter1 = chr(random.randint(97,122))
lowercaseletter2 = chr(random.randint(97,122))
lowercaseletter3 = chr(random.randint(97,122))
lowercaseletter4 = chr(random.randint(97,122))

lowers =  str(lowercaseletter1 + lowercaseletter2 + lowercaseletter3 + lowercaseletter4)

number1 = chr(random.randint(48,57))
number2 = chr(random.randint(48,57))

numbers = str(number1 + number2)

specialcharacter = chr(random.randint(33,47))

password = uppercaseletter1 + shuffle(lowers) + specialcharacter + shuffle(numbers)

print(password)
        
    