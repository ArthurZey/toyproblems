#!/usr/bin/env python3

'''
Introduction
'''

import argparse
import sys
from functools import reduce

def parse_args(args):
  '''Parse arguments into variables readily available to the class for further processing; provides built-in niceties for calling the script from the command line.'''

  parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument("list", help="a quotation-mark-enclosed, comma-separated list of integers;\n\nFor example: \"6, 3, 8, -3, 4, 7, 0, 1, 2, 6, 9, 14\"")
  
  return parser.parse_args(args)

def greatest_product_sublist(input_list):
  # for ease, we're going to pre- and post-pend the input list with zeroes
  input_list = list(input_list)
  output_list = list()

  print("Input list: ")
  print(input_list)

  possible_sublists = [[]]
  for (index, value) in enumerate(input_list):
    if value == 0:
      possible_sublists.append([0]) # this might be duplicative. we can fix this later
      possible_sublists.append(list())
    else:
      possible_sublists[len(possible_sublists) - 1].append(value)

  print("Possible Sublists:")
  print(possible_sublists)

  '''
  start_index = 0
  negatives = list()
  greatest_product = 0
  candidate_list = list()
  for (index, value) in enumerate(input_list):
    if value != 0:
      candidate_list.append(value)
      if value < 0:
        negatives.append((index, value))
    else:
      if reduce(lambda x, y: x*y, candidate_list, 1) > greatest_product:
        output_list = [x for x in candidate_list]
        greatest_product = reduce(lambda x, y: x*y, candidate_list, 1)
        candidate_list = list()
  '''



  return output_list

def main():
  parsed_args = parse_args(sys.argv[1:])

  output_list = greatest_product_sublist(parsed_args.list)
  print(output_list)
  print("Product: " + reduce(lambda x, y: x*y, output_list, 1))
  

if __name__ == '__main__':
  main()