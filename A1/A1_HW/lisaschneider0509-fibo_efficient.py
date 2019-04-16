#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(prog="PROG", description="This program calculates fibonacci numbers. ", add_help=False)

# commandline arguments
parser.add_argument("-n", type=int, help="Any integer")
parser.add_argument("--all", action="store_true", default=False, help="print all fibonacci numbers up to n")
parser.add_argument("--help", "-h", default=False, action="store_true")


# function logic recursive fibonacci
def iterative_fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    else:
        i = 1
        while i < n:
            c = a+b
            a = b
            b = c
            i += 1
        return b


# test parser
DEBUG = False

if DEBUG:
    args = parser.parse_args(["-n", "10", "--all"])
    print(args)
else:
    args = parser.parse_args()

# run recursive fibonacci
number = args.n
printAll = args.all
printHelp = args.help

if printAll and not printHelp:
    i = 1
    while i <= number:
        print(iterative_fibonacci(i))
        i += 1
elif printHelp and not printAll:
    print("Calculate fibonacci numbers.\n"
          "-n an integer > 0 to calculate the nth fibonacci number.\n"
          "--all optional flag to print all fibonacci numbers to n.\n"
          "--help, -h The help site for fibo_inefficient.")
elif not printAll and not printHelp:
    print(iterative_fibonacci(number))
else:
    print("To many arguments")
