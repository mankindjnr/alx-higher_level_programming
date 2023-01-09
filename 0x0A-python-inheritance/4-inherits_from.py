#!/usr/bin/python3
"""
A function that returns true if the object is an instance of a subclass
that inherits directly from a specific class
"""


def inherits_from(obj, a_class):
    """checking if its an instance of a subclass inheriting a specific cls"""
    return issubclass(type(obj), a_class)
