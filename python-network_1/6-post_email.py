#!/usr/bin/python3
"""
This script takes a URL and an email address as arguments, sends a POST request
to the URL with the email as a parameter, and displays the body of the response.

The script uses the `requests` and `sys` packages.
"""

import requests
import sys


if __name__ == "__main__":
    """
    Sends a POST request to the URL with the email as a parameter and displays
    the body of the response.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to send in the POST request
    data = {'email': email}

    # Send a POST request to the URL with the email data
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
