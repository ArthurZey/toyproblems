#!/usr/bin/env python

'''
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

import math

biggest_palendrome = 0

def is_palendrome(string):
  for i in range(0, math.floor(len(string)/2) + 1):
    if string[i] != string[i*(-1)-1]:
      return False
  return True

for i in range(100,1000):
  for j in range(i, 1000):
    if is_palendrome(str(i*j)):
      if i*j > biggest_palendrome:
        biggest_palendrome = i*j

print(biggest_palendrome)