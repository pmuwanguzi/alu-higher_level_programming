#!/usr/bin/python3
"""
This script takes a URL as an argument, sends a GET request to the URL, and
displays the body of the response. If the status code is 400 or higher,
it prints the error code with the HTTP status code.
"""

import requests
import sys


if __name__ == "__main__":
    """
    Sends a GET request to the URL and displays the body of the response.
    If the status code is 400 or greater, it prints the error code.
    """

    # Send a GET request to the URL
    response = requests.get(sys.argv[1])

    # Check if status code is 400 or > and print the error message
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        # Print out the body of the response if status code is < 400
        print(response.text)
