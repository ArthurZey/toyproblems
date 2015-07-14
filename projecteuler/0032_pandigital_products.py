#!/usr/bin/env python

'''
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def is_pandigital(multiplicand, multiplier, product):
  full_string = str(multiplicand) + str(multiplier) + str(product)
  if len(full_string) == 9:
    for i in range(1, 10):
      if str(i) not in full_string:
        return False
    return True
  else:
    return False

pandigitals_products = set()

for multiplicand in range(1, 100):
  for multiplier in range(100, 9999):
    if is_pandigital(multiplicand, multiplier, multiplicand * multiplier):
      pandigitals_products.add(multiplicand * multiplier)

print(sum(pandigitals_products))