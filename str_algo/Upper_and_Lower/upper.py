#coding: utf-8
#this algo allows to transform all the charatcer of a string in uppercase without use upper function




def lowerToUpper(str):
    result_str = ""
    for i in str:
        i_dec = ord(i)
        if i_dec >= 97 and i_dec<= 122:
            i_dec = i_dec - 32
            i_upper = chr(i_dec)
            result_str += i_upper
        else: 
            result_str += i 
    return result_str

s = "HugUes!!"
print(lowerToUpper(s))
