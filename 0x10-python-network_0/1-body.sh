#!/bin/bash
# This script sends a GET request to the URL passed as the first argument
# and displays the body of the response only if it is a 200 status code response.

curl -sL "$1"
