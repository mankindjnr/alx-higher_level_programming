#!/usr/bin/python3
"""creating an object from a json file"""
import json


def load_from_json_file(filename):
    """using json.load() to create an object from a json file"""
    with open(filename, mode="r")as objectfile:
        data = json.load(objectfile)

        print(data)
