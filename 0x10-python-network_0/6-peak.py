#!/usr/bin/env python3
"""Module

`6-peak`: Contains a function `find_peak`
"""


def peak_recursive(a, Min, Max):
    """ Binary Search Recursion """

    if not a:
        return None

    half = int((Max + Min) / 2)

    if (half - 1) < Min and (half + 1) > Max:
        return a[half]

    if (half - 1) < Min and (half + 1) <= Max and a[half + 1] <= a[half]:
        return a[half]

    if (half + 1) > Max and (half - 1) >= Min and a[half - 1] <= a[half]:
        return a[half]

    if (half - 1) >= Min and a[half - 1] <= a[half] \
       and (half + 1) <= Max and a[half + 1] <= a[half]:
        return a[half]

    if a[half + 1] > a[half]:
        return peak_recursive(a, half + 1, Max)

    return peak_recursive(a, 0, half - 1)


def find_peak(list_of_integers):
    """ Find the peak number in a list of integers

    Args:
        list_of_integers (_list_): _A list of integers_

    Returns:
        _int_: _The peak number_
    """

    if not list_of_integers or len(list_of_integers) == 0:
        return None

    Min = 0
    Max = len(list_of_integers) - 1

    return peak_recursive(list_of_integers, Min, Max)
