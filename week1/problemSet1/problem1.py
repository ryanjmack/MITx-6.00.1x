"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if
s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

vowel_count = 0
vowels = "aeiou"
for char in s:
    if char in vowels:
        vowel_count += 1
print("Number of vowels: " + str(vowel_count))
