#!/usr/bin/python3
"""## Remove character in a string at a specific index
"""


def remove_char_at(str, n):
    new_word = list(str)
    for index in range(len(new_word)):
        if index == n:
            new_word.remove(new_word[index])
    return ''.join(new_word)
