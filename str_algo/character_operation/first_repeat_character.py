#coding utf-8
#this algo allows to recover the first character repeat in a str

s = "django framework"

def repeatCharacter(str):
    new_s = ""
    for l in str:
        if l in new_s:
            return(l)
        else:
            new_s += l
            
a = repeatCharacter(s)
print(a)
    
