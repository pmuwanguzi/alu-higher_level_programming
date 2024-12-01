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
    url = "https://api.github.com/user"
    response = get(url, auth=(argv[1], argv[2]))
    print(response.json().get("id"))
