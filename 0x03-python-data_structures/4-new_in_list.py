#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        return my_list
    elif idx > length:
        return my_list

    new_list = []
    for i in range(0, length):
        new_list.append(my_list[i])

    new_list[idx] = element
    return new_list
