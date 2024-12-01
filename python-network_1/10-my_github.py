#!/usr/bin/python3
"""
This script takes in a GitHub username and personal access token (as password),
and uses the GitHub API to display the user ID.
It uses Basic Authentication with the username and
personal access token to access
the GitHub user information.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    """
    Sends a GET request to the GitHub API using the provided credentials
    and displays the user ID.
    """
    username = sys.argv[1]
    token = sys.argv[2]

    # Define the GitHub API URL
    url = "https://api.github.com/user"

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        # If the response is successful, print the user ID
        user_data = response.json()
        print(user_data.get("id"))
    else:
        pass
