#!/bin/bash
# displays all HTTP methods the server will accept.
curl -Is $1 | grep "HTTP/1.1" | awk '{print $2}'
