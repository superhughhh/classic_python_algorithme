# coding: utf-8
#this algo enable to get numeric character in str and make a list that contains each numeric character

import re


s = 'Python 3.0, sorti en 2008 et complètement révisé en 2020'

def numeric_character(str):
    numeric_character = [] 
    
    for character in s:
        if character.isnumeric():
            numeric_character.append(character)
        else:
            continue
        
    return numeric_character
            

a = numeric_character(s)
print(a)