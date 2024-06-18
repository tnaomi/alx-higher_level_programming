#!/usr/bin/python3
""" Handle errors using urllib """

if __name__ == "__main__":
    from urllib import request as R, error as E
    from sys import argv

    url = str(argv[1])
    try:
        with R.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except E.HTTPError as EH:
        print("Error code: {}".format(EH.code))
