#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        print(f"Body respoonse:\n\t\
- type: {type(response)}\n\t\
- content: {response.read()}\n\t\
- utf8 content: {'Ok' if response.readable() else 'No'}")
