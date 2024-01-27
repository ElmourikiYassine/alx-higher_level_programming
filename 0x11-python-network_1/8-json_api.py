#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1]

    payload = {'q': q}
    response = requests.post(url, data=payload)
    try:
        if response.json():
            print(f"[{response.json()['id']}] {response.json()['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
