# coding: utf-8
# this algo allows to swap uppercase to lowercase and vice versa

s = "Hello Word!"
str = ""

def upperLowerInversed(str):
    s_inversed =""
    for i in str:
        u = i.upper()
        l = i.lower()
        if i == l:
            s_inversed += u
        elif i == u:
            s_inversed += l
        else:
            s_inversed == i
    return s_inversed

a = upperLowerInversed(s)
print(a)
