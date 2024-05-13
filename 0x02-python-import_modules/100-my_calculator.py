#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit

    n_operands = len(argv)

    if n_operands != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]

        """match argv[2]:
            case "+":
                result = a + b
            case "-":
                result = a - b
            case "*":
                result = a * b
            case "/":
                result = a / b
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)"""
#  Removed because match is not available in Python3.8xxx
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = (a / b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {}".format(a, op.strip(), b, result.__round__()))
