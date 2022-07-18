# -*- coding: utf-8 -*-
#this algo allows to apply to a list of numbers and an integer n, and returns the number of elements in the list that are divisible by n

list_number = [2, 3, 4, 6, 7, 9, 10,]
number = 40

def nombreDivisibles(integer, list):
    n_dvi = []
    for n in list:
        if (integer % n == 0):
            n_dvi.append(n)
    return n_dvi

list_of_nd = nombreDivisibles(number, list_number)
print(list_of_nd)