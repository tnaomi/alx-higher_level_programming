#!/bin/bash
# Curl and respond with a custom msg
curl -sL -X PUT -d user_id=98 -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
