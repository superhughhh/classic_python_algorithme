# -*- coding: utf-8 -*-
#this algo enable to check the position of a character into a str input

s = input("Tapez la valeur de s : ")

# get the len of the str
n = len(s)

# here, we iterate the index to verify the position of the character
for i in range(0,n):
    
    if(s[i] == 'a'):#with the slice
        
        print("Le caractère  'a' se trouve à la  position : ", i , " dans la chaine s")