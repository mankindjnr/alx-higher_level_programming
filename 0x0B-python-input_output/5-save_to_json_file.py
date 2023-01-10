#!/usr/bin/python3
"""writing an object to text file using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """function to write an object to a text file using JSON repre"""
    with open(filename, "w")as json_file:
        json.dump(my_obj, json_file)
