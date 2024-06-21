#!/usr/bin/python3
""" Contains function `save_to_json_file` """
import json


def save_to_json_file(my_obj, filename):
    """ Dumps the `JSON` representation of an object (string) to a file """
    with open(file=filename, mode="w+", encoding="utf-8") as f:
        json.dump(my_obj, f, skipkeys=True)
