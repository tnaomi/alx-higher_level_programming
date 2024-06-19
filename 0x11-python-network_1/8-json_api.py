#!/usr/bin/python3
""" JSON handling using Requests"""


if __name__ == "__main__":
    import requests as R
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    # url = "https://httpbin.org/post"
    if len(argv) >= 2:
        data = {"q": str(argv[1])}
    else:
        data = {"q": ""}
    try:
        response = R.request("POST", url=url, data=data)
        res_json = response.json()
        if res_json:
            print("[{}] {}".format(res_json.get("id"), res_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
