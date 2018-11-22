#!/usr/bin/env python3

'''
Given a base and a number of digits, find the longest Kaprekar Chain (number of iterations to get to the Kaprekar Constant for that base and number of digits).
'''

import argparse
import sys

def parse_args(args):
  '''Parse arguments into variables readily available to the class for further processing; provides built-in niceties for calling the script from the command line.'''

  parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument("-b", "--base", default="10", type=int, help="the natural number base")
  parser.add_argument("digits", type=int, help="the number of digits for which to find a constant (default: 10)")

  return parser.parse_args(args)

def reverse_number(number):
  return(int(str(number)[::-1]))

def chain_generator(number, base):
  chain = [number]

  return chain

def main():
  parsed_args = parse_args(sys.argv[1:])

  print(parsed_args.digits)
  print(parsed_args.base)

if __name__ == '__main__':
  main()
