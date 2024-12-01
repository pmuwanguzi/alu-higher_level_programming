#!/usr/bin/python3
"""
This script takes in a letter, sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter, and displays the response
based on the JSON content.

Using only requests and sys packages and putting error handling
into consideration.
"""

import requests
import sys


def main():
    """
    Sends a POST request to the specified URL with a letter as the `q` parameter.
    Handles the response, displaying either the user id and name, or error messages
    for invalid JSON, or empty JSON results.
    """
    letter = "" if len(sys.argv) < 2 else sys.argv[1]

    # Define the URL and payload
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    # Send a POST request to the URL
    response = requests.post(url, data=data)

    try:
        # Attempt to parse the response as JSON
        json_response = response.json()

        if json_response:
            # If the JSON is not empty, display the id and name
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            # If the JSON is empty, display No result
            print("No result")

    except ValueError:
        # If JSON is invalid, print error message
        print("Not a valid JSON")
