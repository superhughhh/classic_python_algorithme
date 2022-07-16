# coding: utf-8
#this algo enable to test if a number is ""


a = int(input("Saisir un nombre"))
premier = 0

for n in range(1,a+1):
    if a%n==0:
        premier += 1
    
if premier ==2:
    print(f"{a} est un nombre premier")
else:
    print(f"{a} n'est pas un nombre premier")