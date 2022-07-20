# coding utf-8
##This algorithm allows you to rewrite a string by replacing the odd numbered indices with '#

s = "Python"
len_s = len(s)
new_s =""

for i in range(0,len_s):
    if i%2 == 0:
        new_s += s[i]
    else:
        new_s += "#"
        
print(new_s)
        