#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    content = response.read()
    print(response.headers.get("X-Request-Id"))
