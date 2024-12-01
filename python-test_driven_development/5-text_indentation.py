#!/usr/bin/python3
"""
A script that takes in a text and then prints it
with 2 new lines after each of eith: ., ?, and :.
It expects a string to operate.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ?, and :.

    Parameters:
    text (str): The text to process and print.

    Raises:
    TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    #each occurrence of ., ?, and : with the character newlines
    result = ""
    for char in text:
        result += char
        if char in ".:?":
            result += "\n\n"

    # Split the result into lines,strip whitespace and print
    lines = result.split("\n")
    for line in lines:
        if line.strip():  # Skip empty lines
            print(line.strip())
