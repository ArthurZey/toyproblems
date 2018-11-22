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

  def test_chain_generator(self):
    inputs_to_outputs = {
      (947,10):[947,495],
      (6174,10):[6174,3087,8352,6174],
      (111,10):[]
    }
    for (input, output) in inputs_to_outputs.items():
      self.assertEqual(chain_generator(input[0], input[1]), output)

  def test_all_digits_the_same(self):
    inputs_to_outputs = {
      111:True,
      222:True,
      0:True,
      1:True,
      5555:True,
      33:True,
      72:False,
      7773:False,
      111115:False,
      12:False,
      224:False,
      3962:False
    }
    for (input, output) in inputs_to_outputs.items():
      self.assertEqual(all_digits_the_same(input), output)

if __name__ == '__main__':
  unittest.main()
