#!/bin/bash
# displays all HTTP methods the server will accept.
curl -s -o /dev/null -w "%{http_code}" "$1"
