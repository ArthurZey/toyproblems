#!/usr/bin/env python

'''
https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math

factorians = set()

# upper bound: https://en.wikipedia.org/wiki/Factorion
for i in range(10, 1854722):
  if i == sum([math.factorial(int(d)) for d in str(i)]):
    factorians.add(i)

print(sum(factorians))