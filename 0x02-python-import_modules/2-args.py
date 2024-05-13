#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    its = len(argv)
    if its == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(its - 1))
        for it in range(1, (its)):
            print("{}: {}".format(it, argv[it]))
