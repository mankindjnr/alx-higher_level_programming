#!/usr/bin/python3
"""python3 -c 'print(__import__("2-square").__define_square__)'"""


class Square:
    """python3 -c 'print(__import__("Square").MyClass.__define_class__)'"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
