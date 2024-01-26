#!/bin/bash
# sends a GET request to the URL, and displays the body of the response

#curl -L -s -X GET $1
curl -sX GET $1 -L
