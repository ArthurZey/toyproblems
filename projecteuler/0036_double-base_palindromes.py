#!/usr/bin/env python

'''
https://projecteuler.net/problem=36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import math

def is_palendrome(string):
  for i in range(0, math.floor(len(string)/2) + 1):
    if string[i] != string[i*(-1)-1]:
      return False
  return True

print(sum([i if is_palendrome(str(i)) and is_palendrome(bin(i)[2:]) else 0 for i in range(1, 1000000)]))