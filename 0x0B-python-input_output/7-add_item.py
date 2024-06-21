#!/usr/bin/python3
""" Load, add, save
Contains function `save_to_json_file` & `load_from_json_file`
"""


if __name__ == "__main__":
    from sys import argv
    j_save = __import__('5-save_to_json_file').save_to_json_file
    j_load = __import__('6-load_from_json_file').load_from_json_file

    items = j_load("add_item.json")
    if len(argv) < 2:
        items.append("")
    else:
        items.extend(argv[1:len(argv)])
    j_save(items, "add_item.json")
