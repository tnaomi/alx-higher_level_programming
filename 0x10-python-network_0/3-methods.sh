#!/bin/bash
# Display all methods the Server will accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-
