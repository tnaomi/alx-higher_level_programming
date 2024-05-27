#!/usr/bin/python2
"""Module

`101-lazy_matrix_mul` - Uses `numpy`
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Matrix multiplication using Numpy

    Args:
        `m_a` (matrix): First matrix of lists
        `m_b` (matrix): Second matrix of lists

    Returns:
        _list_: New matrix w the sum of `m_a` and `m_b`
    """
    return np.matmul(m_a, m_b)
