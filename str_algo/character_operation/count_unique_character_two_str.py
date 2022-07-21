#coding utf-8
#this algo allows to count how many unique character are common between two differents str


s = "Hello"
s2 = "World"

def numberOfCommonCharacter(str1, str2):
    list = []
    for i in str1:
        if i in str2:
            list.append(i)
    my_set = set(list)
    result = len(my_set)
    return result

a = numberOfCommonCharacter(s,s2)

print(a)
            
            
        
        


