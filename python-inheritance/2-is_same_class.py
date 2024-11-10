#!/usr/bin/python3
"""Defining a class"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class
    """
    if type(obj) == a_class:
        return True
    return False
