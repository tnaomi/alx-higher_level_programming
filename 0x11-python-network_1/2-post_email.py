#!/usr/bin/python3
""" POST data using urllib """

if __name__ == "__main__":
    from urllib import request as R, parse as P
    from sys import argv

    url = str(argv[1])
    emailaddress = str(argv[2])
    try:
        data = P.urlencode({"email": emailaddress})
        data = data.encode("ascii")
        rq = R.Request(url, data)
        with R.urlopen(rq) as response:
            body = response.read().decode("utf-8")
        print(body)
    except Exception:
        pass
