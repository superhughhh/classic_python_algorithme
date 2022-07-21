#coding utc-8
#this algo allows to recover the most long word present in 2 string


T1 = 'Python created by Guidorossum is open source programming language. Python was created on 1991'
T2 = "Python created by Guidorossum is the most popular programming language Guidorossum"

list_t1 = T1.split(" ")
list_t2 = T2.split(" ")
common_word = []
max_common_word = []
real_max_common_word = []

for word in list_t1:
    if word in list_t2:
        common_word.append(word)

len_max = 0
for word in common_word:
    if len(word) >= len_max:
        len_max = len(word)

for word in common_word:
    if len(word) == len_max:
        real_max_common_word.append(word)
        
print(real_max_common_word)
        
    
    

        