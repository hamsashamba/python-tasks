from collections import Counter

def are_anagrams(string1, string2):
    return Counter(string1) == Counter(string2)

str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

if are_anagrams(str1, str2):
    print(f"{str1} and {str2} are anagrams!")
else:
    print(f"{str1} and {str2} are not anagrams.")