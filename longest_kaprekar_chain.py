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
  return number[::-1]

def all_digits_the_same(number):
  for i in range(1, len(number)):
    if number[i] != number[i-1]:
      return False

  return True

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def chain_generator(number, base, max_length):
  # If all digits of the number are the same, we need to return an empty chain.
  if all_digits_the_same(number):
    return []

  # Initialize the chain with the seed number.
  chain = [number]

  for i in range(max_length):
    number_ascending = "".join(sorted(str(chain[-1])))
    number_descending = "".join(sorted(str(chain[-1]), reverse=True))
    new_number = toStr(abs(int(number_ascending, base)-int(number_descending, base)),base).zfill(len(number))
    if new_number != chain[-1]:
      chain.append(str(new_number))
    else:
      return chain

  # At this point, the for loop completed, so we didn't find a Kaprekar Constant. To indicate the error, we retun an empty chain.
  return []

def first_number(digits):
  return "".join(["1"] + ["0" for x in range(digits - 1)])


def main():
  parsed_args = parse_args(sys.argv[1:])

  base = int(parsed_args.base)
  digits = int(parsed_args.digits)
  max_length = int(parsed_args.max_length)

  # Might want to clean this up with validation on the arguments at call time. Also think about how to extend to bases past 10.
  if base >= 2 and base <= 10 and digits >= 3:
    kaprekar_constants = {}
    kaprekar_divergents = {}
    for i in range(int(first_number(digits), base), int("".join([str(base - 1) for x in range(digits)]), base)):
      number = toStr(i, base)
      chain = chain_generator(number, base, max_length)
      if not all_digits_the_same(number):
        if chain != []:
          if chain[-1] not in kaprekar_constants:
            kaprekar_constants[chain[-1]] = []
          kaprekar_constants[chain[-1]].append({number:len(chain)})
        else:
          kaprekar_divergents[number] = True

      # print(number + ": " + str(chain))
      '''
      print("For " + digits + "-digit numbers in base " + base + ",")
      if no_terminus:
        print(" no Kaprekar Constant could be found within " + max_length + " iterations.")
      else:
        print(" the longest Kaprekar Chain found was")
      '''

    for (kaprekar_constant, constant_properties) in kaprekar_constants.items():
      print(kaprekar_constant)


  print(parsed_args.digits)
  print(parsed_args.base)


if __name__ == '__main__':
  main()
