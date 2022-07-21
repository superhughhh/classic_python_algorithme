#this algo enable to identify a commons words into many str

c = "Bonjour je m'appelle Hugues le filou"
d = "Bonjour je suis Hugh el filou"

def get_common_words(a:str, b:str):
    a_list = a.split(" ")
    b_list = b.split(" ")
    list_of_commons_words = []
    
    for word in a_list:
        if word in b_list:
            list_of_commons_words.append(word)
    
    return list_of_commons_words

commons_words = get_common_words(c, d)
print(commons_words)