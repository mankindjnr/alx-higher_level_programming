#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
implementation of a rectangle following task 8-rectangle
"""


def Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
