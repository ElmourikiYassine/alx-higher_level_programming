#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response.
   You have to manage urllib.error.HTTPError exceptions and print:
   Error code: followed by the HTTP status code"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
