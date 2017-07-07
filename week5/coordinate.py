# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:02:50 2017

@author: ryanj

OOP practice
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __repr__(self):
        return "Coordinate({},{})".format(self.getX(), self.getY())

a = Coordinate(3, 4)
b = Coordinate(1, 2)
c = Coordinate(1, 2)

print(a)
print(b == c, a == c)
print(repr(c1))
