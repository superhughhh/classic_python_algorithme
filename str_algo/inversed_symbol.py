# coding: utf-8
#this algo enable make symbol like this
#******
#*****
#****
#***
#**
#*


n = int(input("input line number : "))
 
symbol = '*'
for j in range(n , 0 , -1):
    for i in range(j , 0 , -1):
        print(symbol , end = ' ')
    print('\r')
 