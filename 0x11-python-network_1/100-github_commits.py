#!/usr/bin/python3
""" Github API handling using Requests"""


if __name__ == "__main__":
    import requests as R
    from sys import argv

    repo = str(argv[1])
    owner = str(argv[2])
    passwd = str(argv[3])
    header = {"User-Agent": "tnaomi", "Accept": "application/vnd.github+json",
              "X-GitHub-Api-Version": "2022-11-28",
              "Authorization": "Bearer {}".format(passwd)}
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    try:
        response = R.request("GET", url=url, headers=header)
        res_json = response.json()
        if res_json:
            if len(res_json) < 10:
                length = len(res_json)
            else:
                length = 10
            for i in range(length):
                if res_json[i]["commit"] and res_json[i]["commit"]["author"]:
                    """
                    # To get the full name [ANOTHER `LONGER` METHOD]
                    user = res_json[i]["author"].get("login")
                    url1 = "https://api.github.com/users/{}".format(user)

                    try:
                        response1 = R.request("GET", url=url1,
                        headers=header).json()
                        if response1:
                            print("<{}>: <{}>".format(res_json[i]["sha"],
                            res_json[i]["commit"]["author"].get("name")))
                    except ValueError:
                        print("None")
                    """
                    full_name = res_json[i]["commit"]["author"].get("name")
                    print("{}: {}".format(res_json[i]["sha"], full_name))
        else:
            print("None")
    except ValueError:
        print("None")
