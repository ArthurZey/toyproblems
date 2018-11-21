#!/usr/bin/env python3

from longest_kaprekar_chain import *
import unittest

class KaprekarTestCases(unittest.TestCase):
  def test_reverse(self):
    inputs_to_outputs = {
      1:1,
      10:1,
      153:351,
      100:1,
      101:101,
      220:22,
      260:62
    }
    for (input, output) in inputs_to_outputs.items():
      self.assertEqual(reverse_number(input), output)

if __name__ == '__main__':
  unittest.main()
