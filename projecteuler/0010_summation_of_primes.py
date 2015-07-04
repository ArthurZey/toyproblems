#!/usr/bin/env python

'''
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

def prime_sum(n):
  # we start with the knowledge of at least one prime
  primes = [2]

  # and the next possible prime is the next odd number
  number_to_test = 3

  # we're going to grow the primes list until we have the prime that's just before n
  while number_to_test < n:
    # start with the default assumption that number_to_test is prime
    is_prime = True

    # since, by construction, all the primes less than number_to_test have already been found,
    # we need only test the possible_divisors in primes up to the square root of number_to_test
    # to see if they divide number_to_test before confirming or disproving that number_to_test
    # is indeed prime
    for possible_divisor in primes:
      if possible_divisor >= math.floor(math.sqrt(number_to_test)) + 1:
        is_prime = True
        break
      
      if number_to_test%possible_divisor == 0:
        is_prime = False
        break
      
    if is_prime:
      primes.append(number_to_test)
    
    # in any event, move on to the next candidate (the next odd number)
    number_to_test += 2

  return sum(primes)

print(prime_sum(2000000))