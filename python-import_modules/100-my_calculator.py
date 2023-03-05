#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    import sys
    first_number =sys.argv[0]
    second_number = sys.argv[2]
    operator = sys.argv[1]
    first_number = int(first_number)
    second_number = int(second_number)
    operator = str(operator)
    if first_number or second_number or operator == False:
        print("Usage: ./100-my_calculator.py a operator b")
    elif operator != "+" or "-" or "*" or "/":
        print("Unknown operator. Available operators: +, -, * and /")
    elif operator == "+":
        print("{} + {} = {}".format(first_number, second_number, add(first_number, second_number)))
    elif operator == "-":
        print("{} - {} = {}".format(first_number, second_number, sub(first_number, second_number)))
    elif operator == "*":
        print("{} * {} = {}".format(first_number, second_number, mul(first_number, second_number)))
    elif operator == "/":
        print("{} / {} = {}".format(first_number, second_number, div(first_number, second_number)))


    
