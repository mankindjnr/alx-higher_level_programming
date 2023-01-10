#!/usr/bin/python3
"""a script that adds all arguments to a python list and save them to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    items_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    items_list = []

for item in sys.argv[1:]:
    items_list.append(item)

save_to_json_file(items_list, "add_item.json")


"""
This script starts by importing the functions save_to_json_file() and
load_from_json_file() from the provided file.

The script will try to load from the json file and if it does not exist a
FileNotFoundError will be raised, the script will catch the exception and
create an empty list instead of loading the json.

Then it will iterate through the arguments passed to the script (excluding the
script name itself) and append each argument to the list.

Finally, the script uses the save_to_json_file() function to save the list to
the "add_item
"""
