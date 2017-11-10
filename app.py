#!/usr/bin/python3

import sys
import argparse

print("hellow world")

parser = argparse.ArgumentParser(description="")
parser.add_argument('--inventory', '-i', nargs='?',help='filepath with environement varible set')
args= parser.parse_args(sys.argv[1:])
if args.inventory:
    print(args.inventory)

else:
    print("argument not passed !!!!!")


