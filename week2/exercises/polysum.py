"""
Created on Fri Jun  9 15:58:35 2017

@author: ryanjmack
"""
import math

def polysum(n, s):
    """
    input:
    n: number of sides
    s: length of one side

    output:
    Sum the area and square of the perimeter of the regular polygon.
    The function returns the sum, rounded to 4 decimal places.
    """

    perimeter_squared = (n * s)**2
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    output = perimeter_squared + area

    return round(output, 4)
