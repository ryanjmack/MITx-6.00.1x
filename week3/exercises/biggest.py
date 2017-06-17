# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:57:40 2017

@author: ryanmack
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    output = {'key': None, 'length': 0}

    for key in aDict:
        length = len(aDict[key])
        if length > output['length']:
            output = {'key': key, 'length': length}

    # return the key that has the largest value
    print(output['key'])



animals = {'a': ['aardvark'],
           'b': ['baboon'],
           'c': ['coati'],
           'd': ['donkey', 'dog', 'dingo']}

# returns 'd'
biggest(animals)
