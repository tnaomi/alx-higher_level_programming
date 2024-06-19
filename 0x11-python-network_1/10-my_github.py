#!/usr/bin/python3
""" Github API handling using Requests"""


if __name__ == "__main__":
    import requests as R
    from sys import argv

    user = str(argv[1])
    passwd = str(argv[2])
    header = {"User-Agent": "tnaomi", "Accept": "application/vnd.github+json",
              "X-GitHub-Api-Version": "2022-11-28",
              "Authorization": "Bearer {}".format(passwd)}
    url = "https://api.github.com/users/{}".format(user)
    try:
        response = R.request("GET", url=url, headers=header)
        res_json = response.json()
        if res_json:
            print("{}".format(res_json.get("id")))
        else:
            print("None")
    except ValueError:
        print("None")
