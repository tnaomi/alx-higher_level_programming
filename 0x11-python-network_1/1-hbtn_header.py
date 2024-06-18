#!/usr/bin/python3
""" Request an URL and display X-Request-Id """

if __name__ == "__main__":
    import urllib.request as UR
    from sys import argv

    xr = ""
    if len(argv) != 2:
        xr = ""
    else:
        url = str(argv[1])
        try:
            with UR.urlopen(url) as response:
                xr = response.info().get('X-Request-Id')
        except Exception:
            pass
    print(xr)
