#!/usr/bin/python3
"""define class Rectangle that inherit from the BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialise new Rectangle

        Args:
            width - int: width of new Rectangle
            height - int: height of new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
