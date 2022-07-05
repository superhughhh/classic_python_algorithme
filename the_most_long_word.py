from cgitb import reset


#this algo enable to find a most long word in str given
my_str = "Un chasseur sachant chasser sans son chien est un bon chasseur"


def theMostLongWord(str):
    
    list_str = str.split(" ")

    lens_word_most_long = 0

    for mot in list_str:
        lens_mot = len(mot)
        if lens_mot > lens_word_most_long:
           word_most_long = mot
           
    return word_most_long

result = theMostLongWord(my_str)
print(result)

        
