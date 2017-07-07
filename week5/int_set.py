# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 12:03:45 2017

@author: ryanjmack

Practice using OOP priniciples
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """Returns a new intSet containing elements that appear in both sets"""
        newSet = intSet()

        for num in other.vals:
            if self.member(num):
                newSet.insert(num)

        return newSet

    def __len__(self):
        return len(self.vals)

a = intSet()
a.insert(1)
a.insert(2)

b = intSet()
b.insert(1)
b.insert(2)
b.insert(3)

print(b)
print(a)
print(len(b))
