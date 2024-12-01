#!/usr/bin/python3
"""A Python script that fetches https://alu-intranet.hbtn.io/status
using the urllib package."""
from urllib import request

if __name__ == "__main__":
    with request.urlopen(
            "https://alu-intranet.hbtn.io/status"
            if "https://intranet.hbtn.io/status".startswith("https")
            else "https://intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))
