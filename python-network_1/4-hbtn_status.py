#!/usr/bin/python3
"""
a Python script that fetches https://alu-intranet.hbtn.io/status
"""


import requests


if __name__ == "__main__":
    """
    Sends a GET request to 'https://alu-intranet.hbtn.io/status', get's back the
    response then displays the type, content, and decoded content of the body
    of the response.
    """
    url = 'https://alu-intranet.hbtn.io/status'

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the body of the response details
    print("Body response:")
    print("    - type: {}".format(type(response.text)))
    print("    - content: {}".format(response.text))
    print("    - utf8 content: {}".format(response.text.encode('utf-8').decode('utf-8')))
