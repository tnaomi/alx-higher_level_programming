#!/usr/bin/bash
# Curl a JSON POST and display the result
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
