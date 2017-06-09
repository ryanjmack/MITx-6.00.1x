"""
Created on Fri Jun  9 15:33:31 2017

@author: ryanjmack
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise

    We can use the idea of bisection search to determine if a character is in
    a string, so long as the string is sorted in alphabetical order.=
    '''

    if len(aStr) <= 1:
        return True if aStr == char else False

    middle = len(aStr) // 2

    if char == aStr[middle]:
        return True
    elif char > aStr[middle]:
        return isIn(char, aStr[middle + 1:])
    elif char < aStr[middle]:
        return isIn(char, aStr[0:middle])
