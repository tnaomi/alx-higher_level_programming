#!/usr/bin/python3
""" Request an URL and display status """

if __name__ == "__main__":
    import urllib.request as UR
    url = "https://alx-intranet.hbtn.io/status"
    with UR.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
