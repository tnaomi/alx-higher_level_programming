#!/usr/bin/python3
""" Request an URL and display status using Requests"""

if __name__ == "__main__":
    import requests as R

    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = R.get(url).text
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
    except Exception:
        pass
