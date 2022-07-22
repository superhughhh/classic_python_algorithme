#coding: utf-8
##this algo allows to identify words with at least one uppercase and regroup the result in the list

s = 'Python is more power thant Java and C++'
my_list = s.split(" ")
upper_list = []

for word in my_list:
    lower = word.lower()
    if word != lower:
        upper_list.append(word)
   
print(upper_list)
        