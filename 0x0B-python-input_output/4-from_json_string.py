#!/usr/bin/python3
"""returning an object from JSON string"""
import json


def from_json_string(my_str):
    """converting a json string into a python object"""
    data = json.loads(my_str)

    return data
