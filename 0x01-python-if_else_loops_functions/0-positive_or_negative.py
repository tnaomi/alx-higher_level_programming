#!/usr/bin/python3
""" Print if a number is positive or negative or zero """
import random
number = random.randint(-10, 10)

if number > 0:
    print(f"{{}} is positive".format(number))

elif number == 0:
    print(f"{{}} is zero".format(number))

else:
    print(f"{{}} is negative".format(number))
