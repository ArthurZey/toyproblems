#!/usr/bin/env python3

'''
Given a base and a number of digits, find the longest Kaprekar Chain (number of iterations to get to the Kaprekar Constant for that base and number of digits).

Additional Resources:
https://www.math.hmc.edu/funfacts/ffiles/10002.5-8.shtml
http://kaprekar.sourceforge.net/output/sample.php
http://mathworld.wolfram.com/KaprekarRoutine.html
https://plus.maths.org/content/mysterious-number-6174
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
    print(number_ascending + " - " + number_descending + " = " + new_number)
    if new_number != chain[-1]:
      chain.append(str(new_number))
    else:
      return chain

  # At this point, the for loop completed, so we didn't find a Kaprekar Constant. To indicate the error, we retun an empty chain.
  return []

def first_number(digits):
  return "".join(["1"] + ["0" for x in range(digits - 1)])

def results(digits, base, max_length):
  # Might want to clean this up with validation on the arguments at call time. Also think about how to extend to bases past 10.
  if base >= 2 and base <= 10 and digits >= 3:
    for i in range(int(str(pow(10,digits-1)), base), int("".join([str(base-1) for x in range(digits)]), base)):
      number = toStr(i, base)
      chain = chain_generator(number, base, max_length)
      if not all_digits_the_same(number):
        if chain != []:
          yield (number, {"constant": chain[-1], "length": len(chain)})
        else:
          yield (number, {"constant": None})




def main():
  parsed_args = parse_args(sys.argv[1:])

  base = int(parsed_args.base)
  digits = int(parsed_args.digits)
  max_length = int(parsed_args.max_length)

  kaprekar_constants = {}
  kaprekar_divergents = set()
  for (number, properties) in results(digits, base, max_length):
    if properties["constant"] is not None:
      if properties["constant"] in kaprekar_constants:
        kaprekar_constants[properties["constant"]].add(properties["length"])
      else:
        kaprekar_constants[properties["constant"]] = {properties["length"]}
    else:
      kaprekar_divergents.add(number)

  if len(kaprekar_constants) > 0:
    print("For " + str(digits) + "-digit numbers in base " + str(base) + ", the following Kaprekar Constants were found (with corresponding longest chains):")
    for kaprekar_constant in kaprekar_constants:
      print(str(kaprekar_constant) + " (max chain length: " + str(max(kaprekar_constants[kaprekar_constant])) + ")")
    if len(kaprekar_divergents) > 0:
      print("The following numbers did not converge within chains of length " + str(max_length) + ": " + str(kaprekar_divergents))
  else:
    print("For " + str(digits) + "-digit numbers in base " + str(base) + ", no Kaprekar Constants were found within chains of length " + str(max_length) + ".")


  # print(parsed_args.digits)
  # print(parsed_args.base)


if __name__ == '__main__':
  main()
