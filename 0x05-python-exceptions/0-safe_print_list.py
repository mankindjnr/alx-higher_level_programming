#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    count = 0

    for mylist in my_list:
        length += 1;

        try:
            for i in range(0, x):
                print("{}".format(my_list[i]), end='\n')
                count += 1
        except:
            pass
        return count
