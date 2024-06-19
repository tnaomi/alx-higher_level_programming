# 0x11-python-network_1

## Author

Tadala N. Kapengule

## Tasks

### 0. What's my status? #0

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- You must use the package `urllib`
- You are not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before `-`)
- You must use a `with` statement

__File__
`0-hbtn_status.py`

### 1. Response header value #0

Write a *Python* script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

- You must use the packages `urllib` and `sys`
- The value of this variable is different for each *request*
- You are not allow to import packages other than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use a `with` statement

__File__
`1-hbtn_header.py`

### 2. POST an email #0

Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the `email` as a parameter, and displays the body of the response (decoded in `utf-8`)

- The email must be sent in the `email` variable
- You are not allow to import packages other than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use a `with` statement

__File__
`2-post_email.py`

### 3. Error code #0

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

- You have to manage `urllib.error.HTTPError exceptions` and print: `Error code:` followed by the HTTP status code
- You are not allow to import packages other than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use a `with` statement

__File__
`3-error_code.py`

### 4. What's my status? #1

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- You must use the package `requests`
- You are not allow to import packages other than `requests`
- The body of the response must be display like the following example (tabulation before `-`)

__File__
`4-hbtn_status.py`

### 5. Response header value #1

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`
- The value of this variable is different for each request
- You don’t need to check script arguments (number and type)

__File__
`5-hbtn_header.py`

### 6. POST an email #1

Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

- The email must be sent in the variable `email`
- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`
- You don’t need to check script arguments (number and type)

__File__
`6-post_email.py`

### 7. Error code #1

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

- If the HTTP status code is greater than or equal to `400`, print: `Error code:` followed by the value of the HTTP status code
- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`
- You don’t need to check script arguments (number and type)

__File__
`7-error_code.py`

### 8. Search API

Write a Python script that takes in a *letter* and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

- The letter must be sent in the variable `q`
- If no argument is given, set `q=""`
- If the response body is properly `JSON` formatted and not empty, display the id and name like this: `[<id>] <name>`
- Otherwise:
- - Display `Not a valid JSON` if the `JSON` is invalid
- - Display `No result` if the `JSON` is empty

- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`

__File__
`8-json_api.py`

### __OPTIONAL <> <> <> TASKS__

### 9. My GitHub'!'

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

- You must use [Basic Authentication](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with a [personal access token as password](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28) to access to your information (only `read:user` permission is needed)
- The first argument will be your `username`
- The second argument will be your `password` (in your case, a [personal access token as password](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28))
- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`
- You don’t need to check script arguments (number and type)

__File__
`10-my_github.py`

### 10. Time for an interview'!'

Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)

Write a Python script that takes 2 arguments in order to solve this challenge.

- The first argument will be the `repository` name
- The second argument will be the `owner` name
- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`
- You don’t need to check script arguments (number and type)

__File__
`100-github_commits.py`
