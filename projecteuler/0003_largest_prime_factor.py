#!/usr/bin/env python

'''
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import math

def find_factors(number):
  factors = set()
  for index in range(2, math.floor(math.sqrt(number))+2):
    if number == 2:
      factors.add(2)
    elif number%index == 0:
      factors = factors.union(find_factors(index))
      factors = factors.union(find_factors(int(number/index)))
  if len(factors) == 0:
    factors.add(number)
  return factors

print(max(find_factors(600851475143)))




