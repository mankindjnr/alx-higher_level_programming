#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable in the header of the resp.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        X_Request_Id = resp.headers.get('X-Request-Id')
        print(X_Request_Id)
