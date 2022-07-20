# coding: utf-8
#this algo allows to transform a list of str 

import os

List_programming_books = ["Python programming books", "Java programming books", "C ++ programming books", "C # programming books"]
file = open("List_programming_books.txt" , "w")
for item in List_programming_books:
    file.write(item + "\n")

file.close()

#print txt file in terminal
file = open("List_programming_books.txt" , "r")
for line in file:
    print(line, end="")