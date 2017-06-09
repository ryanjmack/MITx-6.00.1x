"""
Created on Fri Jun  9 09:50:49 2017

@author: ryanjmack
"""

def square(x):
    '''
    x: int or float.
    '''
    return x**2


def fourthPower(x):
    '''
    x: int or float.
    output: x to the fourth power
    '''
    return square(square(x))
