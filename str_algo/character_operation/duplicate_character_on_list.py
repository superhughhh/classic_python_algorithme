# coding: utf-8
#this algo allows to identify a duplicates characters in str and return a lsi with these characters

a = "django framework"

 

def DuplicateCharacterOnList(str):
    r = ""
    list = []
    
    for i in str:
        if i in r:
            list.append(i)
        else:
            r +=i
    return list
    
    
c = DuplicateCharacterOnList(a)
print(c)
