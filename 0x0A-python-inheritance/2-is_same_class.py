#!/usr/bin/python3
"""a function returns true if obj is an instance of the specified class"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    else:
        return False
