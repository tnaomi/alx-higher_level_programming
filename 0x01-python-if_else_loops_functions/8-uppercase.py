#!/usr/bin/python3
""" Prints a string in uppercase """


def uppercase(str):
    """# Print a string in uppercase.
    #### Don't  use `str.upper` or `str.isupper`
    """
    List = []
    for c in str:
        uni = ord(c)
        if uni in range(97, 97+26):
            List.append(c.capitalize())
        else:
            List.append(c)

    f_string = ''.join(List)
    print("{}".format(f_string))
