#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

mod = number % 10

print("Last digit of", number, "is", mod, end=" ")
if mod > 5:
    print("and is greater than 5")
elif mod == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0 ", end="\n")
