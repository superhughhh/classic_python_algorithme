# -*- coding: utf-8 -*-
# this algo allows to identify count the upercase and the lowercase in a str

s = "Je Suis Un Dev"

def CountUpperAndLower(str):
    n_of_l = 0
    n_of_u = 0
    for l in s:
        if l != " ":
            low = l.lower() 
            if l == low:
                n_of_l += 1
            else:
                n_of_u += 1
    return (n_of_l, n_of_u)

a = CountUpperAndLower(s)
print(f"dans {s}, il y a {a[0]} minuscule et {a[1]} majuscule")