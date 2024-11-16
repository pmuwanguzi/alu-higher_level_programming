#!/usr/bin/python3
"""this is a function that returns the json representation
of an object  (string)"""
import json


def to_json_string(my_obj):
    """A function to returning a json  with object: string"""
    data = json.dumps(my_obj)
    return data
