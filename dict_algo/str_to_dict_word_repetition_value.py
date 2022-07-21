#coding utf-8
#this algorithm takes as parameter a string s and returns the dictionary whose keys are the words that compose the string s and whose key values are the number of occurrences of the words in the string Text s.

s = "I use Python for datascience but I don't use Python for mobile"

def wordOccurrnce(str):
    
    d = {}
    list_s = str.split(" ")

    for word in list_s:
        d[word] = list_s.count(word)
        
    return d

a = wordOccurrnce(s)
print(a)
