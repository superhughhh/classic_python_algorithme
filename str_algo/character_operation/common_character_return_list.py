#coding utf-8
#this algo allows to check the common characters between two string and retrieves them as a list.

s1 = 'Python language'
s2 = 'Java Programming'
tup = (s1,s2)


def commonCharacter(tup):
    list_common = []
    list_result = []
    for i in tup[0]:
        if i in tup[1] and i not in list_common:
            list_common.append(i)
    return list_common

a = commonCharacter(tup)
print(a)