"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print

Longest substring in alphabetical order is: abc
"""

largest = ""

for i in range(len(s)):

    # cache the ascii value of s[i] in prev
    prev = ord(s[i])
    j = i + 1

    # iterate over the characters in s after s[i]
    while j < len(s):

        # check to see if ascii value of s[j] >= prev ascii value
        if ord(s[j]) >= prev:
            prev = ord(s[j])
            j += 1

        # if not break
        else:
            break

    #now time for some checks; temp is the current substring
    temp = s[i:j]

    # set the largest alphabetical substring to temp if it's bigger
    if len(temp) > len(largest):
        largest = temp

print("Longest substring in alphabetical order is: " + largest)
