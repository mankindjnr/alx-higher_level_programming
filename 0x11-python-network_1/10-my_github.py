#!/usr/bin/python3
"""
my github with basic auth using github api
"""
import sys
import requests

if __name__ == "__main__":
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://docs.github.com/en/rest/users?apiVersion=2022-11-28"
    response = requests.get(url, auth=(user_name, passwd))
    try:
        print(response.json()["id"])
    except KeyError:
        print("None")
