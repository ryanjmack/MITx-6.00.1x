"""
Created on Thu Jun 15 10:48:15 2017

@author: ryanmack
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    output: int, how many values are in the dictionary.
    '''
    # each value in aDict is a list
    values = aDict.values()
    output = 0

    # x is a list
    for x in values:
        output += len(x)

    return output

# data
animals = {'a': ['aardvark'],
           'b': ['baboon'],
           'c': ['coati'],
           'd': ['donkey', 'dog', 'dingo']}

# returns 6 animals
how_many(animals)
