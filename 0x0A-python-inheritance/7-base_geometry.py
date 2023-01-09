#!/usr/bin/python3
"""improving the geometry class from 6-geometry.py"""


class BaseGeometry:
    """validating  name and values and raising errors"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be gretaer than 0".format(name))
