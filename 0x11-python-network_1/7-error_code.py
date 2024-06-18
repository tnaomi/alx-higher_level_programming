#!/usr/bin/python3
""" Error handling using Requests"""


if __name__ == "__main__":
    import requests as R
    from sys import argv

    url = str(argv[1])
    try:
        response = R.request("GET", url=url)
        RE = response.status_code
        if RE > 400:
            print(f"Error code: {{}}".format(RE))
        else:
            print(response.text)
    except Exception:
        pass
