#!/usr/bin/python3
"""function that JSON serializes an object"""
import json


def class_to_json(obj):
    """JSON serializing"""
    def default(o):
        return o.__dict__
    return json.dumps(obj, default=default)
