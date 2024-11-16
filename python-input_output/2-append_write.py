#!/usr/bin/python3
"""This is function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8) and returns the number of characters added."""
    if not filename:
        print("Filename is required.")
        return 0

    if len(text) > 10000:  # Arbitrary limit for excessively long text
        print("Text is too long to append.")
        return 0

    try:
        with open(filename, "a", encoding="utf-8") as file:
            return file.write(text)
    except FileNotFoundError:
        print(f"File '{filename}' does not exist. Creating a new file.")
        with open(filename, "w", encoding="utf-8") as file:
            return file.write(text)
