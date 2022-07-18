# coding: utf-8
#this algo allows to recover a first duplicate character into a str

a = "django framework"
b = "abricot"
 

def first_duplicate_character(str):
    r = ""
    no_duplicate = "No duplicate character"
    
    for i in str:
        if i in r:
            return i
        else:
            r +=i
    return no_duplicate
    
    
c = first_duplicate_character(a)
d = first_duplicate_character(b)
print(c)
print(d)

            
            

