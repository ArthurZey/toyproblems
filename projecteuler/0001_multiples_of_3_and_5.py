#!/usr/bin/env python

'''
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''



index = 1
multiples = set()

while index * 3 < 1000:
  multiples.add(index * 3)
  index += 1

index = 1

while index * 5 < 1000:
  multiples.add(index * 5)
  index += 1

print(sum(multiples))