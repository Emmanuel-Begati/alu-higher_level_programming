#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    import sys
    first_number =sys.argv[1]
    second_number = sys.argv[3]
    operator = sys.argv[2]
    first_number = int(float(first_number))
    second_number = int(float(second_number))
    operator = str(operator)
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py a operator b")
    elif operator == "+":
        print("{} + {} = {}".format(first_number, second_number, add(first_number, second_number)))
    elif operator == "-":
        print("{} - {} = {}".format(first_number, second_number, sub(first_number, second_number)))
    elif operator == "*":
        print("{} * {} = {}".format(first_number, second_number, mul(first_number, second_number)))
    elif operator == "/":
        print("{} / {} = {}".format(first_number, second_number, div(first_number, second_number)))
    elif operator != "+" or "-" or "*" or "/":
        print("Unknown operator. Only: +, -, * and / available")
