#!/usr/bin/env python

'''
https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.
Hence the first 12 terms will be:

F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144
The 12th term, F(12), is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

f_n_minus_2 = 1
f_n_minus_1 = 1
f_n = 0


n = 3
while len(str(f_n)) < 1000:
  f_n = f_n_minus_1 + f_n_minus_2

  f_n_minus_2 = f_n_minus_1
  f_n_minus_1 = f_n
  n += 1

print(n-1)