# coding utf-8
# this algo allows to recover a list of duplicate character in a str


def isRepeted(s,x):
    counter = 0
    for i in s:
        if i == x:
            counter +=1
            
    if counter >= 2:
        return True
    else:
        return False

def repetedCharacter(s):
    list_result = []
    for i in s:
        if isRepeted(s,i) and i not in list_result and i !=" ":
            list_result.append(i)
    return list_result
            

str = "Programming language"
a = repetedCharacter(str)
print(a)

