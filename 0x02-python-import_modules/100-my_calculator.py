#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    c = len(argv)

    if c != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    num_1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]

    def notfound():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def my_add():
        total = add(num_1, num2)
        print("{:d} + {:d} = {:d}".format(num_1, num2, total))
        return total

    def my_sub():
        total = sub(num_1, num2)
        print("{:d} - {:d} = {:d}".format(num_1, num2, total))
        return total

    def my_mul():
        total = mul(num_1, num2)
        print("{:d} * {:d} = {:d}".format(num_1, num2, total))
        return total

    def my_div():
        total = div(num_1, num2)
        print("{:d} / {:d} = {:d}".format(num_1, num2, total))
        return total

    options = {
        "+": my_add,
        "-": my_sub,
        "*": my_mul,
        "/": my_div
    }
    options.get(op, notfound)()
