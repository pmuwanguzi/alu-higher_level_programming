#!/usr/bin/python3
"""Defining a function"""


def is_kind_of_class(obj, a_class):
    """Write a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
