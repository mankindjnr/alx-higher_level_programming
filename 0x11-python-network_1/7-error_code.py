#!/usr/bin/python3
"""
outputing error codes and detecting them
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    code_status = response.ok
    if code_status is True:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
