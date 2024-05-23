#!/usr/bin/python3
def magic_calculation(a, b):
    """ Magic calculator

    Args:
        a (_int_) : First operand
        b (_int_) : Second operand

    Returns:
        _int_ : binary number
    """

    result = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return (result)
