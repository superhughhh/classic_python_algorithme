# -*- coding: utf-8 -*-
#this algo allows to add "*" between every letter of a str

s = "Python"

def InsertEtoile(str):
    list = []
    for l in s:
        list.append(l)
    new_str = "*".join(list)
    return new_str
    
    
a = InsertEtoile(s)
print(a)
    