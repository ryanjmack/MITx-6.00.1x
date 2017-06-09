# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:55:31 2017

@author: ryanjmack
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    return a if b == 0 else gcdRecur(b, a % b)
