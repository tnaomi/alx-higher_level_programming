#!/usr/bin/bash
# Send a POST request and display the response
curl -s "$1" -X POST -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD'
