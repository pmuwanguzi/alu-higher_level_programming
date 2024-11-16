#!/usr/bin/python3
"""This is function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""

    with open(filename, "a", encoding="utf-8")as file:
        file.write(text)
