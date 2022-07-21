#coding: utf-8
#this algo allows to find the first occurrence of s1 found in the string s without using any predefined function, and return the index.

def Find(s , s1):
    n = len(s)
    m = len(s1)
    k = -1
    for i in range(0 , n):
        if s[i:i+m] == s1:
            k = i
            break
    return k

s = "Python language" 
s1 = "lang"
print(Find(s , s1))      # affiche  7
print(Find(s , 'land')) #  affiche  -1