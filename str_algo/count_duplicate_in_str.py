# -*- coding: utf-8 -*-
#this algo enable to count how many a character is present in a str

s = "Python est un langage de programmation"
# we use set to add a single character (because a set doesn't tolerate duplicates character)
unique = set({})
for x in s:
    if x not in unique:
        unique.add(x)#the single character are added in the set
        print("Le nombre d'occurrences du caractère: ", x, " dans la chaine s est :", s.count(x))
        # we have just to count the duplicate character with 'count function'
        