#!/usr/bin/python3
"""function that JSON serializes an object"""


def class_to_json(obj):
    """converting an object attri to a dictionary for JSON serialization"""
    obj_dict = {}
    for key in obj.__dict__:
        obj_dict[key] = obj.__dict__[key]

    return obj_dict
