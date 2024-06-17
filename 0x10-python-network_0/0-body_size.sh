#!/bin/bash
# Get content size from a cURL request response
curl -sI "$1" | grep "Content-Length:" | cut -d ' ' -f2
