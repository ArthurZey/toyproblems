#!/usr/bin/env python

'''
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

import math

def prime(n):
  # we start with the knowledge of at least one prime
  primes = [2]

  # and the next possible prime is the next odd number
  number_to_test = 3

  # we're going to grow the primes list until we have the n-th prime
  while len(primes) < n:
    # if the number we're testing is prime
    if is_prime(number_to_test, primes):
      # add it to the primes list
      primes.append(number_to_test)
    
    # in any event, move on to the next candidate (the next odd number)
    number_to_test += 2

  # return the last prime
  return primes[-1]
    


# note that is_prime only returns True for the next prime after those in known_primes
def is_prime(number, known_primes):
  # by hypothesis, we've already found all the primes up to number (they're in the known_primes list)
  # that means that if number is composite, it will be in this list
  for possible_divisor in known_primes:
    # if the possible_divisor divides evenly into number, number is not prime
    if number%possible_divisor == 0:
      return False
    
    # break out early if we've already reached the square root and haven't found any divisors
    if possible_divisor >= math.floor(math.sqrt(number)) + 1:
      return True

  # if we've gone through all the known_primes and haven't found a divisor, this is a prime!
  return True

print(prime(10001))