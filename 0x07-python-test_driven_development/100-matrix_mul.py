#!/usr/bin/python3
"""Module

`100-matrix_mul`: Multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices. Appropriate error handling

    Args:
        m_a (_matrix_): First matrix. Size: `m x n`
        m_b (_matrix_): Second matrix. Size: `m x n`

    Returns:
        _list_: a matrix w the result of `m_a` * `m_b`
    """
    msg_a, msg_em = "m_a must be a list", "m_a can't be empty"
    msg_type = "m_a should contain only integers or floats"
    msg_len = "each row of m_a must be of the same size"
    result, mult = [], 1
    if type(m_a) is not list:
        raise TypeError(msg_a)
    elif type(m_b) is not list:
        raise TypeError(msg_a.replace("m_a", "m_b"))
    elif not all(type(i) is list for i in m_a):
        raise TypeError(msg_a.__add__(" of lists"))
    elif not all(type(i) is list for i in m_b):
        raise TypeError(msg_a.replace("m_a", "m_b").__add__(" of lists"))
    elif len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError(msg_em)
    elif len(m_b) == 0 or (len(m_a) == 1 and len(m_b[0]) == 0):
        raise ValueError(msg_em.replace("m_a", "m_b"))

    result = [False if type(j) not in [int, float] else True
              for i in m_a for j in i]
    if False in result:
        result.clear()
        raise TypeError(msg_type)
    result = [False if type(j) not in [int, float] else True
              for i in m_b for j in i]
    if False in result:
        result.clear()
        raise TypeError(msg_type.replace("m_a", "m_b"))
    result = []

    for row in m_a:
        if len(row) not in result:
            result.append(len(row))
    if len(result) != 1:
        raise ValueError(msg_len)
    result.clear()
    for row in m_b:
        if len(row) not in result:
            result.append(len(row))
    if len(result) != 1:
        raise TypeError(msg_len.replace("m_a", "m_b"))
    result.clear()

    try:
        for i in range(len(m_a)):
            n_row = [sum([m_a[i][k] * m_b[k][j] for k in range(len(m_b))])
                     for j in range(len(m_b[0]))]
            result.append(n_row)
    except Exception:
        raise ValueError("m_a and m_b can't be multiplied")
    return result
