#!/usr/bin/python3
"""a class myclass that inherits from list"""

class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
