#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = []
    if idx < 0 or idx > length:
        return my_list

    for i in range(length):
        if i != idx:
            new_list.append(my_list[i])
        else:
            new_list.append(element)
    return new_list
