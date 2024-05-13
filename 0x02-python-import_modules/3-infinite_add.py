#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    its = len(argv)
    if its == 1:
        print(0)
    else:
        sum = 0
        for it in range(1, (its)):
            sum += int(argv[it])
        print("{}".format(sum))
