#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
The libraries used are `urllib` and `sys`
Error handling is applied.
"""

import urllib.request
import sys
import urllib.error


def main():
    """
    This is the Main entry point of the script. It Takes the URL
    from the command-line, sends it as a GET request and retrieves
    the response and prints out the body.
    """
    url = sys.argv[1]

    try:
        # Send a GET request to the URL and retrieve the response
        with urllib.request.urlopen(url) as response:
            # Read the response body and decode it in UTF-8
            body = response.read().decode('utf-8')

        # Print the body of the response
        print(body)

    except urllib.error.HTTPError as e:
        # Handle HTTPError and print the error code
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
