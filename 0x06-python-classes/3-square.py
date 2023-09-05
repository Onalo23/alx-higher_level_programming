#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """initialise a new square

        Arguments:
            size-int: size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return current area of square"""
        return (self.__size * self.__size)