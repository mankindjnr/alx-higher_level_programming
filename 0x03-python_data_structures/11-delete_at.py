#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < 0:
        return my_list
    elif idx > length:
        return my_list

    my_list[idx:idx + 1] = []

    return my_list
