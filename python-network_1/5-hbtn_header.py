#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in
the response header.
Using only request and sys package.
"""


import requests
import sys

if __name__ == "__main__":
    """
    Takes the URL from the command-line
    arguments, sends a GET request,
    then prints the value of the `X-Request-Id`
    header from the response.
    """
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Fetch and print the X-Request-Id header value
    print(response.headers.get('X-Request-Id'))

