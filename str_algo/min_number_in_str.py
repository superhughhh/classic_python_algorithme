#coding utf-8
#This algo allows to find all the int in str and recover the min int

s = "Python3.7 est plus puissant que Python2.7"

def minNumberInStr(str):

    digit_list = []
    for i in str:
        if i.isdigit():
            digit_list.append(i)

    min_number = digit_list[0]

    for i in digit_list:
        if i < min_number:
            min_number = i
    return min_number
        
a = minNumberInStr(s)
print(a)