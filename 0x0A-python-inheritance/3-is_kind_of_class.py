#!/usr/bin/python3
"""returns true if the object is an instnce of or the subclass"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of class or a sublass"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
