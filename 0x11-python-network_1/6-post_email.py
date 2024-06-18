#!/usr/bin/python3
""" POST data using Requests"""

if __name__ == "__main__":
    import requests as R
    from sys import argv

    url = str(argv[1])
    emailaddress = str(argv[2])
    try:
        data = {"email": emailaddress}
        response = R.request("POST", url=url, data=data)
        print(response.text)
    except R.exceptions:
        pass
