##This algo compare two list,check the missing elements and create a list with them

list_a = [4, 2, 7, 1]


def missing_element(list_to_check, min_interval, max_interval):
    
    list_ME = []
    for i in range (min_interval,max_interval+1):
        if i not in list_a:
            list_ME.append(i)
    return list_ME     

list_ME = missing_element(list_a,1, 10)
print(list_ME)

