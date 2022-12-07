#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]

    for key in a_dictionary:
        print(f"{key}: {a_dictionary[key]}")
