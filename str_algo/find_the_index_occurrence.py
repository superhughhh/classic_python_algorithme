#coding utf-8
#this algo allows to search an occurence and return its index if it's present in a string

s = "langage de programmation Python" 
occ = "de "

def indexOfOccurence(str, occurrence):
    len_s = len(str)
    len_occ = len(occurrence)
    index = -1
    for l in range(0, len_s):
        if s[l:l+len_occ] == occurrence:
            index = l
            return index
    return index


a = indexOfOccurence(s, occ)
print(a)