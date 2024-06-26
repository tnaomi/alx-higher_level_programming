#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """### Add the individual elements of 2 tuples

    Args:
        tuple_a (tuple, optional): First tuple. Defaults to ().
        tuple_b (tuple, optional): Second tuple. Defaults to ().
    """
    count_a = len(tuple_a)
    count_b = len(tuple_b)

    if count_a == 0:
        tuple_a = (0, 0)
    if count_b == 0:
        tuple_b = (0, 0)

    if count_a == 1:
        tuple_a = (tuple_a[0], 0)
    if count_b == 1:
        tuple_b = (tuple_b[0], 0)

    sum1 = tuple_a[0] + tuple_b[0]
    sum2 = tuple_a[1] + tuple_b[1]

    return (sum1, sum2)
