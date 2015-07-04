#!/usr/bin/env python

'''
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product a * b * c.
'''


# certainly far from the most efficient solution, but it allows us to do it in one line using a list comprehension!
print([
  a * b * c
  
  for a in range(1, 1000)
  for b in range(a, 1000)
  for c in range(b, 1000)
  
  if a + b + c == 1000
    and a < b               # possibly unnecessary, given the constraints in the for clause
    and b < c               # possibly unnecessary, given the constraints in the for clause
    and a**2 + b**2 == c**2
  ][0])