# -*- coding: UTF-8 -*-
#this algo allows to delete the void str in a list

list_inp = ["Python" , "" , "is" , "" , "the",  "most" , "", "used" , "programming", "language" , ""]

list_out = []
for i in list_inp:
    if i != "":
        list_out.append(i)
print(list_out)
    