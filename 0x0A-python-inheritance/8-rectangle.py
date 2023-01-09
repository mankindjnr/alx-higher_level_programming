#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""inheriting a class from another module"""


class Rectangle(BaseGeometry):
    """class rectangle instantiation"""
    def __init__(self, width, height):
        self._width = width
        self._height = height
        # validating values with no getter or setter from a function
        # in the base class by using a method in the sub class
        super().integer_validator("width", self._width)
        super().integer_validator("height", self._height)
