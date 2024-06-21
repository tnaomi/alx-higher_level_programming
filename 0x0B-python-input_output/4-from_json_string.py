#!/usr/bin/python3
""" Contains function `from_json_string` """
import json


def from_json_string(my_str):
    """ Constructs an obj representation from a JSON string """
    return json.loads(my_str)
