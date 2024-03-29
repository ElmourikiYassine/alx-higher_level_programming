#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response.
   You have to manage urllib.error.HTTPError exceptions and print:
   Error code: followed by the HTTP status code"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
