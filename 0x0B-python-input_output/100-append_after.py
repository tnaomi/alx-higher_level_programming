#!/usr/bin/python3
""" Contains function `append_after` """


def append_after(filename="", search_string="", new_string=""):
    """ Appends a string after a search string to a file in `utf-8` """
    with open(filename, mode="r+", encoding="utf-8") as f:
        line_list = []
        lines = f.readlines()
        for i in range(len(lines)):
            line_list.append(lines[i])
            if search_string in lines[i]:
                line_list.append(new_string)
        f.seek(0)
        f.write("".join(line_list))
