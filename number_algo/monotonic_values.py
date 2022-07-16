# this algo enable to know if a list of values is monotonic or not

def monotone_value(list):
    m = 0
    for n in list:
        if n >= m:
            result = "monotonic values"
        else: 
            result = "not monotic values"
            return result
        m = n
    return result          
        

a = [1, 1, 2, 4, 8, 9, 11, 11, 14]
b = [1, 2, 3, 5, 7, 6, 10, 11, 11]
c = [12, 3]

values_set = [a, b, c]


for i in values_set:
    result = monotone_value(i)
    print(f"the set '{i}' is {result}")
    