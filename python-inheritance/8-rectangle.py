#!/usr/bin/python3
"""Defining a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
        Instantiation with width and height: def __init__(self, width, height):
        width and height must be private. No getter or setter
        width and height must be positive integers, validated by integer_validator
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
