# coding utf-8
#this algo allows to the most the most frequency occurence(s) in a str and retrieve the result as a list.
#I'm sick of it ^^

s = "Programmming"

def maxOccurrence(str):
    result_list = []
    list_s = []
    counter_max = 1
    for l in str:
        x = str.count(l)
        if x >= counter_max:
            counter_max = x
        y = (l,x)
        if y[1] == counter_max and y not in list_s:
            list_s.append(y)
    for i in list_s:
        if i[1] == counter_max:
            result_list.append(i[0])
    return result_list


a = maxOccurrence(s)
print(a)


