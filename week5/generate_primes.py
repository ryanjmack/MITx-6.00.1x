"""
Created on Sun Jul  9 09:30:40 2017

@author: ryanjmack
"""

def genPrimes():
    """
    generator that returns the sequence of prime numbers
    on successive calls to its next() method
    """
    # offer the first, and only even prime number
    yield 2

    # simple prime generator
    n = 3
    while True:
        if isPrime(n):
            yield(n)
        n += 2

# https://en.wikipedia.org/wiki/Primality_test#Simple_methods
def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i +=  6
    return True
