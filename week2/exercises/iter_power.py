# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:08:04 2017

@author: ryanmack
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''

    product = 1
    while(exp >= 1):
        product *= base
        exp -= 1

    return product
