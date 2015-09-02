#!/usr/bin/env python3

'''
https://en.wikipedia.org/wiki/Insertion_sort
'''

import argparse
import sys

def parse_args(args):
  '''Parse arguments into variables readily available to the class for further processing; provides built-in niceties for calling the script from the command line.'''

  parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument("list", help="a quotation-mark-enclosed, comma-separated list of integers;\n\nFor example: \"6, 3, 8, -3, 4, 7, 0, 1, 2, 6, 9, 14\"")
  
  return parser.parse_args(args)

def parse_input_string(input_string):
  return [int(x) for x in "".join([c for c in input_string if c in "0123456789-,"]).split(",")]


def insertion_sort(input_list):
  output_list = list(input_list)

  # Go through each element
  for i in range(1, len(output_list)):
    # print(output_list)
    value = output_list[i]
    # print("  considering index " + str(i) + ": " + str(value))
    # Iterate backward until the right place is found
    if value < output_list[i - 1]:
      for j in range(i - 1, -1, -1):
        # Scoot each guy one spot forward
        output_list[j+1] = output_list[j]
        
        # If we've gotten all the way back to the front or our value is between two consecutive values, we're found the right spot. Break out of the inner for loop.
        if j == 0 or (value >= output_list[j-1] and value <= output_list[j]):
          output_list[j] = value
          break

  return output_list

def main():
  parsed_args = parse_args(sys.argv[1:])
  print("Insertion Sort:")
  print(insertion_sort(parse_input_string(parsed_args.list)))

if __name__ == '__main__':
  main()