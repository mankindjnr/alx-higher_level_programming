#!/usr/bin/python3
"""function that JSON serializes an object"""
import json


def class_to_json(obj):
    """JSON serializing by defininta default method to return the dict"""
    def default(o):
        """
        defining a default method that returns a dictionary rep of that
        object and the json.dumps to serialize the object with the default
        parameter set to the default method defined above
        """
        return o.__dict__
    return json.dumps(obj, default=default)
