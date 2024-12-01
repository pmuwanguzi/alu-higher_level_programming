#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response using only packages urllib and sys"""
import urllib.request
import sys

def main():
    """
    Here the script takes the URL from the command-line
    arguments and sends a GET request, and prints the X-Request-Id from the
    response headers.
    """
    url = sys.argv[1]
    
    # Send a GET request to the URL and retrieve the response headers
    with urllib.request.urlopen(url) as response:
        # Retrieve the value of the X-Request-Id header
        request_id = response.getheader('X-Request-Id')
    
    # Print the value of the X-Request-Id header
    print(request_id)

if __name__ == "__main__":
    main()

