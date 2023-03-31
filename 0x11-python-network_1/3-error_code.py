#!/usr/bin/python3
"""
write ython code that takes in a URL, sends request to the url and
displays the body of the response secded in utf-8
"""
from urllib import request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as resp:
            print(resp.read()).decode("utf-8")
    except HTTPError as e:
        print("Error code: {}".format(e.code))
