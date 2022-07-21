#coding: utf-8
#this algo allows to count the occurence/word and their numbers of appearance in a string and and retrieve the result as a dictionary
s = "je suis Hugues et je commence a bien maitriser le langage de programmation Python"

def count_the_character(str):
    my_dict = {}
    for i in str:
        y = s.count(i)

        if i not in my_dict and i != " ":
            my_dict.update({i:y})
            #mydict[i] = y
    return(my_dict)

def count_the_words(str):
    my_list = str.split(" ")
    my_dict = {}
    for word in my_list:
        y = my_list.count(word)
       
        if word not in my_dict:
            my_dict.update({word:y})
            #mydict[word] = y
    return my_dict

a = count_the_character(s)
b = count_the_words(s)
print(a)
print(b)


