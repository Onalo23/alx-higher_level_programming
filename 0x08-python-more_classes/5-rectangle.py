#!/usr/bin/python3
"""define Rectangle class"""


class Rectangle:
    """represents rectangle"""

    def __init__(self, width=0, height=0):
        """initialise new Rectangle

        Arguments:
            width- int: width of new rectangle
            height- int: height of new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return printable representation of Rectangle

        Represents rectangle with the #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for p in range(self.__height):
            [rect.append('#') for q in range(self.__width)]
            if p != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return string representation of Rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print message for every deletion"""
        print("Bye rectangle...")
