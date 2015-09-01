#!/usr/bin/env python3

'''
Introduction
'''

import argparse
import sys

class MyClass:
  def __init__(self, args):
    self.parsed_args = self.parse_args(args)

  def __str__(self):
    '''Explanation of what output might look like.'''
    
    return "This is a mighty fine instance of MyClass!"

  def parse_args(self, args):
    '''Parse arguments into variables readily available to the class for further processing; provides built-in niceties for calling the script from the command line.'''

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    # In the following lines, add all the parser.add_argument() calls.
    # "\n" in the 'help' parameter will be interpreted as a line break.
    
    return parser.parse_args(args)

def main():
  my_class_instance = MyClass(sys.argv[1:])
  print(my_class_instance)

if __name__ == '__main__':
  main()