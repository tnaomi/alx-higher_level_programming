#!/usr/bin/python3
"""Returns the power of two numbers"""


def fizzbuzz():
    """Fizzbuzz program
    """

    def _mod(number, operand):
        """Find the modulus of a given number

        Args:
            number (int): The number
            operand (int): the given base

        Returns:
            int: modulus
        """
        mod = number % operand
        return mod if not mod else mod - operand if number < 0 else mod
    for num in range(1, 101):
        if _mod(num, 3) == 0:
            if _mod(num, 5) == 0:
                print('FizzBuzz ', end='')
            else:
                print('Fizz ', end='')
        elif _mod(num, 5) == 0:
            if _mod(num, 3) == 0:
                print('Fizzbuzz ', end='')
            else:
                print('Buzz ', end=' ')
        else:
            print("{} ".format(num), end='')
