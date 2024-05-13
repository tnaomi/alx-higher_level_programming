#!/usr/bin/python3

def magic_calculation(a, b):
    from calculator_1 import add, sub
    if (a < b):
        c = sub(a, b)
        for count in range(4, 6):
            c -= count
        return c
    else:
        sum = add(b, a)
        return sum
