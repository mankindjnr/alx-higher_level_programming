#!/usr/bin/python3
"""a class rectangle that defines a rec by lenght"""


class Rectangle:
    """the rectangle class defined with width and height"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    # width getters and setters
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # height getters and setters
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
