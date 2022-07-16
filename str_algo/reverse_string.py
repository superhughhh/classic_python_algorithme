#this algo allow to reverse a str

#for example : hello => olleh

my_str = "bonjour"

def reverse_string(str):
    result = ""
    for letter in str:
        result = letter + result
    return result
    

inv_str = reverse_string(my_str)
print(inv_str)


#the special hask python version 

str = "SALUT A TOUS"

print(str[::-1])