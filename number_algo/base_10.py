# coding: utf-8
#this algo allows to decomposed a number in base 10 without used function and without the number convert in str

nombre = 1234
n = nombre
milliers = 0
centaines = 0
dizaines = 0
unités = 0


while n > 999:
    n = n - 1000
    milliers +=1
while n > 99:
    n = n - 100
    centaines +=1
while n > 9:
    n = n - 10
    dizaines +=1
while n > 0:
    n = n - 1    
    unités += 1

print(f"{nombre} est composé de {milliers} fois 1000, {centaines} fois 100, {dizaines} fois 10 et {unités} fois 1.")

