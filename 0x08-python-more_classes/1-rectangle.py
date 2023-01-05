#!/usr/bin/python3
"""a class rectangle that defines a rec by lenght"""


class Rectangle:
    """the rectangle class defined with width and height"""
    # private instance attribute width and height
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    # width property getter
    def width(self):
        return self.__width

    # width property setter
    def width(self, value):
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif value < 0:
            raise ValueError("width must be >- 0")
        else:
            raise TypeError("width must be an integer")

    # getter height
    def height(self):
        return self.__height

    # height setter
    def height(self, ValueHeight):
        if isinstance(ValueHeight, int) and ValueHeight >= 0:
            self.__height = ValueHeight
        elif ValueHeight < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
