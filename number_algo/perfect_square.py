# coding: utf-8
#this program enable to know if input number is a 'perfect square'
#perfect square : 4=2x2 or 16=4x4 : 4 and 16 is perfect square


n = int(input("Tapez la valeur de n :  "))
j = 0

for i in range(0,n):
    
    if(i**2 == n):
        j += 1

        
if(j > 0):
    print("L'entier ", n , " est un carré parfait")
    
else:
    print("l'entier ", n , " n'est pas est un carré parfait")