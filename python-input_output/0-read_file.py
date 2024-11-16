#!/usr/bin/python3
"""This is a python function reading text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """A text file (UTF8) is read and its
    content is printed to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
