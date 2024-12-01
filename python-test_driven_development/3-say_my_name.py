#!/usr/bin/python3
"""
A script that prints takes in two values
both being strings and prints "My name is 
first string and second string"
It also checks for errors
"""
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Parameters:
    first_name (str): The first name.
    last_name (str, optional): The last name.
    Defaults to an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
