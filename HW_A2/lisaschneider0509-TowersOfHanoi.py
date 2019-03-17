#!/usr/bin/env python

import argparse
import sys

parser = argparse.ArgumentParser(prog="PROG", description="This program calculates fibonacci numbers. ", add_help=False)

# commandline arguments
parser.add_argument("-n", type=int, help="Any integer")
parser.add_argument("--all", action="store_true", default=False, help="print all fibonacci numbers up to n")
parser.add_argument("--help", "-h", default=False, action="store_true")


# function logic Towers of Hanoi

def hanoi_towers(number, from_peg, to_peg, unused_peg):
    if number == 1:
        first_run = 1
        print(f"Move disk {number} from peg {from_peg} to peg {to_peg}")
        return first_run
    first_run = hanoi_towers(number - 1, from_peg, unused_peg, to_peg)
    print(f"Move disk {number} from peg {from_peg} to peg {to_peg}")
    second_run = hanoi_towers(number - 1, from_peg, to_peg, unused_peg)
    return first_run + second_run + 1


# test parser
DEBUG = False

if DEBUG:
    args = parser.parse_args(["-n", "3"])
    print(args)
else:
    args = parser.parse_args()

# run recursive fibonacci
mynumber = args.n
printHelp = args.help

if printHelp and not mynumber:
    print("Calculate the moves for a towers of hanoi problem with n disks.\n"
          "Print commands to STDOUT and move number to STDERR"
          "-n disk number (integer > 0).\n"
          "--help, -h The help site.")

elif mynumber and not printHelp:
    move_number = hanoi_towers(mynumber, from_peg=1, to_peg=3, unused_peg=2)
    print("\n")
    print(move_number, file=sys.stderr)

else:
    print("To many arguments. --help for help. ")
