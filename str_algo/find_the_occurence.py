# coding utf_8
#this algo allows to check if an occurence given is in string given

def findTheOccurence(o, str):
    for i in str:
        if i == o:
            return True
    return False

a = "Je m'appelle Hugues"
b = "H"
c = "+"

d = findTheOccurence(b,a)
print(d)
e = findTheOccurence(c,a)
print(e)

        