#!/usr/bin/python3
""" Request an URL and display X-Request-Id using Requests"""

if __name__ == "__main__":
    import requests as R
    from sys import argv

    url = str(argv[1])
    try:
        response = R.get(url)
        print(response.headers["X-Request-Id"])
    except Exception:
        pass
