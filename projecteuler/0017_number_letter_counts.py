#!/usr/bin/env python

'''
https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

import math

numbers_as_words = {
   1: "one",
   2: "two",
   3: "three",
   4: "four",
   5: "five",
   6: "six",
   7: "seven",
   8: "eight",
   9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
  1000: "onethousand",
  }

glob = ""

def number_as_words(n):
  if n in numbers_as_words:
    return numbers_as_words[n]
  elif n < 100:
    return "".join([number_as_words(n-(n%10)), number_as_words(n%10)])
  elif n >= 100:
    return "".join([
      number_as_words(int((n-(n%100))/100)),
      "hundred",
      "" if n%100 == 0 else "".join(["and", number_as_words(n-(int(math.floor(n/100))*100))]),
      ])

for i in range(1, 1001):
  glob = "".join([glob, number_as_words(i)])

print(len(glob))

