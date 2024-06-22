#!/usr/bin/python3
""" Contains function `from_json_string` """
import json


def load_from_json_file(filename):
    """ Constructs an obj from a JSON string using `json.load` """
    return json.loads(filename)
