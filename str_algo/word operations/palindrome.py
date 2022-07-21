# -*- coding: utf-8 -*-
# this algo enable to check if a str is a 'palindrome' => laval, radar, sos

mot = input("Saisir un mot : ")

inverse = mot[::-1]
if(mot == inverse):
    print("Le mot :", mot," est un palindrome")
else:
    print("Le mot : ", mot, " n'est pas un palindrome")
 

