#!/usr/bin/env python

'''
https://projecteuler.net/problem=20

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math

amicable_numbers = list()

def d(n):
  sum_of_divisors = 1 # since 1 is always a divisor, no need to check

  for possible_divisor in range(2, math.floor(math.sqrt(n)) + 2):
    if n%possible_divisor == 0:
      sum_of_divisors += possible_divisor
      sum_of_divisors += int(n/possible_divisor)

  return sum_of_divisors

sum_of_amicable_numbers = 0

for i in range(1, 10000):
  if d(d(i)) == i and d(i) != i:
    sum_of_amicable_numbers += i

print(sum_of_amicable_numbers)