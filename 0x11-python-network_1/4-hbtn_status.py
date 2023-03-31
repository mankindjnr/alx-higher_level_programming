#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

req = requests.get("https://alx-intranet.hbtn.io/status")

content_type = req.headers['Content-Type']
if 'text' in content_type:
    content_type = req.text
    print("Body response:")
    print("\t- type: {}".format(type(content_type)))
    print("\t- content: {}".format(content_type))
