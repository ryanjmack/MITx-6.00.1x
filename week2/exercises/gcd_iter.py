"""
Created on Fri Jun  9 10:08:30 2017

@author: ryanjmack
"""

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.

    One easy way to do this is to begin with a test value equal to the
    smaller of the two input arguments, and iteratively reduce this test
    value by 1 until you either reach a case where the test divides both
    a and b without remainder, or you reach 1.
    '''
    divisor = min(a, b)

    while divisor > 1:
        # common divisor found
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        divisor -= 1

    # GCD is 1
    return divisor
