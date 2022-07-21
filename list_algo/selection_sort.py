# -*- coding: UTF-8 -*-
#this algo is the sort by selection

list_to_sorted = [62, 14, 17, 89, 52, 24, 71, 9, 21]
len_list = len(list_to_sorted)
result_list = []
min_value = 100


def sortBySelection():
    for e in list_to_sorted:
        if e < min_value:
            min_value = e
    result_list.append(min_value)


a = sortBySelection(a)
print(result_list)
    