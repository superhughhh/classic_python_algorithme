#this algo enable to count a number of uppercase in str 

my_str = "Hello EverYone"

number_of_uppercase = 0



for i in my_str:
    y = i.lower()
    if i != y:
        number_of_uppercase += 1 
    else:
        number_of_uppercase +=0
        
print(number_of_uppercase)