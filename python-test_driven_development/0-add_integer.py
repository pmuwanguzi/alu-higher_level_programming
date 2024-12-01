#!/usr/bin/python3
"""
A python function that adds two integers.
With the second integer having a default as 98.
It's also puting error handling into consideration.
"""
def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int/float): The first number.
    b (int/float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b, after casting to integers.

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers and return the sum
    return int(a) + int(b)
