#!/bin/bash
# displays all HTTP methods the server will accept.
curl -Is -X GET $1 | grep "Allow" | awk '{printf "%s %s %s\n", $2,$3,$4}'
