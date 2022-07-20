#coding utf-8
#this algo allows to rewrite a str without vowel


s = "Python is hight level programming language"
s_without_vowel =""
vowel = ["a","e","i","o","u","y"]


for i in s:
    if i not in vowel:
        s_without_vowel += i

print(s_without_vowel)
    