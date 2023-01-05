#!/usr/bin/python3
"""a class rectangle that defines a rec by lenght"""


class Rectangle:
    """the rectangle class defined with width and height"""
    # private instance attribute width and height
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # property getter
    def width(self):
        return self.__width

    def height(self):
        return self.__height

    # property setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    # height setter
    def height(self, ValueHeight):
        if not isinstance(ValueHeight, int):
            raise TypeError("height must be an integer")
        if ValueHeight < 0:
            raise ValueError("height must be >= 0")

        self.__height = ValueHeight
