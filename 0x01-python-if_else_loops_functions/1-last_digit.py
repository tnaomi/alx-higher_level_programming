#!/usr/bin/python3
"""Print the mod of a number and fulfill conditional requirements"""
import random
from math import fmod
number = random.randint(-10000, 10000)

mod = fmod(number, 10)

print(f"Last digit of {{}} is {{}}".format(number, int(mod)), end=' ')
if mod > 5:
    print("and is greater than 5")
elif mod == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
