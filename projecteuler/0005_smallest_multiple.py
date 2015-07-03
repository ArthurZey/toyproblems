#!/usr/bin/env python

'''
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
import math

def find_factors(number):
  factors = list()
  for index in range(2, math.floor(math.sqrt(number))+2):
    if number == 2:
      factors.append(2)
    elif number%index == 0:
      factors.extend(find_factors(index))
      factors.extend(find_factors(int(number/index)))
      break
  if len(factors) == 0:
    factors.append(number)
  return factors

final_prime_factors = dict()

for i in range(2, 21):
  i_prime_factors = dict()
  for j in find_factors(i):
    if j in i_prime_factors:
      i_prime_factors[j] += 1
    else:
      i_prime_factors[j] = 1
  for j in i_prime_factors:
    if j in final_prime_factors:
      if i_prime_factors[j] > final_prime_factors[j]:
        final_prime_factors[j] = i_prime_factors[j]
    else:
      final_prime_factors[j] = i_prime_factors[j]

product = 1

for i in final_prime_factors:
  product *= i**final_prime_factors[i]

print(product)