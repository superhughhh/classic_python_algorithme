# -*- coding: utf-8 -*-
#this algo allows to delete excess space in str

str = "Un   texte     avec  beaucoup     trop   d'espace"

list = str.split()
text_without_space = ""

for word in list:
    text_without_space = text_without_space + word + " "
    
    
print(text_without_space)









