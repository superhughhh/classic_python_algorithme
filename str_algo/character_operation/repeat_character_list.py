#coding: utf-8
##This algorithm identifies repeated characters and retrieves them as a list.


s= "Python langage"

def repeatCharacter(str):
    new_s = ""
    repeat_character = []
    for l in str:
        if l in new_s:
            repeat_character.append(l)
        else:
            new_s += l
    return repeat_character
            
a = repeatCharacter(s)
print(a)
    
