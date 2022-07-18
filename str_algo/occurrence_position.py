
# coding: utf-8
# this algo allows to find an occurrence into a str and return a index position of the occurrence.

def rechercher(s , s1):
    n = len(s)
    m = len(s1)
    # initialisation de l'index recherché
    k = -1
    # parcourir les élément de la chaine s et rechercher l'occurrence s1
    for i in range(0 , n-m):
        if s[i:i+m] == s1:
            k = i
            break
    return k

s = "Python Programming" 
s1 = "thon"

print(rechercher(s , s1))      # affiche:  2
print(rechercher(s , 'thons')) # affiche: -1
