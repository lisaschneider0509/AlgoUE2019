#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(prog="PROG", description="This program calculates fibonacci numbers. ", add_help=False)

# commandline arguments
parser.add_argument("-n", type=int, help="Any integer")
parser.add_argument("--all", action="store_true", default=False, help="print all fibonacci numbers up to n")
parser.add_argument("--help", "-h", default=False, action="store_true")


# function logic recursive fibonacci
def recursive_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 1:
        a = recursive_fibonacci(n - 1)
        b = recursive_fibonacci(n - 2)
        return a+b
    elif n == 0:
        return 0


# test parser
DEBUG = False

if DEBUG:
    args = parser.parse_args(["-n", "4", "--all"])
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
        print(recursive_fibonacci(i))
        i += 1
elif printHelp and not printAll:
    print("Calculate fibonacci numbers.\n"
          "-n an integer > 0 to calculate the nth fibonacci number.\n"
          "--all optional flag to print all fibonacci numbers to n.\n"
          "--help, -h The help site for fibo_inefficient.")
elif not printAll and not printHelp:
    print(recursive_fibonacci(number))
else:
    print("To many arguments")
