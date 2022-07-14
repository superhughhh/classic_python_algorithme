# coding: utf-8
#this program enable to concatenate two str with alternative method

a = "Python"
b = "Java"

def alt_concatenation (str_1, str_2):
    
    result = ""
    len1 = len(str_1)
    len2 = len(str_2)
    
    if len1 < len2:
        for i in range(0,len1):
            result = result + str_1[i] + str_2[i]
        result = result + str_2[len1+1 : str_2]
        
    else:
        for i in range(0, len2):
            result = result + str_1[i] + str_2[i]
        result = result + str_1[len2+1 : len1]
    
    return result

c = alt_concatenation(a,b)
print(c)
#PJyatvhan
        
