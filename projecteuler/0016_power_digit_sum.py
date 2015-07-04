#!/usr/bin/env python

'''
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

# in python, 2^1000 (2**1000) returns the full integer
print(sum([int(x) for x in list(str(2**1000))]))
