#!/usr/bin/python3
"""Implementation of the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """the class inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returning the width of the square though its getter"""
        return self.width

    @size.setter
    def size(self, side):
        """setting the width and height throught their setters"""
        self.setter_validation("width", side)
        self.width = side
        self.height = side
