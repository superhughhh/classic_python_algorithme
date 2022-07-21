#coding utf-8
# This algo allows to switch the second character with the second last character in string

s = "Python"
my_list = []

for i in s:
    my_list.append(i)
    

a = my_list[-2]
my_list[-2] = my_list[1]
my_list[1] = a
print(my_list)