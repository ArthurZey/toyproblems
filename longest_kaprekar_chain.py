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
  parser.add_argument("--max_length", default="1000", type=int, help="the maximum length of a chain to search for before calling it quits")

  return parser.parse_args(args)

def reverse_number(number):
  return(int(str(number)[::-1]))

def all_digits_the_same(number):
  number = str(number)

  for i in range(1, len(number)):
    if number[i] != number[i-1]:
      return False

  return True

def chain_generator(number, base, max_length):
  # If all digits of the number are the same, we need to return an empty chain.
  if all_digits_the_same(number):
    return []

  # Initialize the chain with the seed number.
  chain = [number]

  for i in range(max_length):
    number_ascending = "".join(sorted(str(chain[-1])))
    number_descending = "".join(sorted(str(chain[-1]), reverse=True))
    new_number = abs(int(number_ascending)-int(number_descending))
    if new_number != chain[-1]:
      chain.append(new_number)
    else:
      return chain

  # At this point, the for loop completed, so we didn't find a Kaprekar Constant. To indicate the error, we retun an empty chain.
  return []

def main():
  parsed_args = parse_args(sys.argv[1:])

  print(parsed_args.digits)
  print(parsed_args.base)

if __name__ == '__main__':
  main()
