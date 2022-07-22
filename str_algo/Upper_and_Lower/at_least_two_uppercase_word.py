#coding: utf-8
##this algo allows to identify words with at least two uppercase and regroup the result in the list


s = 'La bibliothèque GUI PySide est plus populaire que PyQt'

def AtLeastTwoUppercaseWord(str):
    my_list = str.split(" ")
    upper_list = []
    for word in my_list:
        counter = 0
        for letter in word:
            lower_letter = letter.lower()
            if letter != lower_letter:
                counter += 1
        if counter > 1:
            upper_list.append(word)
    return upper_list
    
a = AtLeastTwoUppercaseWord(s)
print(a)

         