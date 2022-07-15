# -*- coding: utf-8 -*-
#this algo enable to know each divider of a number

n = int(input("input your integer"))

for i in range(1,n+1):

    if(n%i==0):# i test if have a integer divider
        
        print("Le nombre ",i," est un diviseur de  ",n)
 