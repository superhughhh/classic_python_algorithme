

s = "python"

def lowerTo_Upper(str):
    list = []
    list_upp = []
    s_upp = ""
    
    for l in s:
        a = ord(l)
        list.append(a)
        
    for n in list:
        b = n - 32
        c = chr(b)
        list_upp.append(c)
    
    s_upp = "".join(list_upp)
    return s_upp

r = lowerTo_Upper(s)
print(r)
        
    
