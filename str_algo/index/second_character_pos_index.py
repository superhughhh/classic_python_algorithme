#coding: utf-8
#this program allows to return the index of the second position of a duplicate character in a string

s = 'langage python' 
x = 'a'

def indexOfSecondCharacterPosition(str,character):
    len_s = len(str)
    counter = -1
    for i in range(0,len_s):
        if s[i] == character:
            counter +=1
        if counter == 1:
            return(i)
    return counter
        
    
a = indexOfSecondCharacterPosition(s,x)
print(a)