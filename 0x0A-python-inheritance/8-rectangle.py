#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""inheriting a class from another module"""


class Rectangle(BaseGeometry):
    """class rectangle instantiation"""
    def __init__(self, width, height):
        self.integer_validator("width", self._width)
        self.integer_validator("height", self._height)

        self._width = width
        self._height = height
