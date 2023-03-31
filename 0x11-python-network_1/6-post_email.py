#!/usr/bin/python3
"""python script that takes in url"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, payload)
    print(response.text)
