#!/usr/bin/python3
"""define class Rectangle that inherit from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents rectangle with BaseGeometry"""

    def __init__(self, width, height):
        """Intialise new Rectangle

        Arguments:
            width - int: width of new Rectangle
            height - int: height of new Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return print() and str() representation of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
