#!/usr/bin/env python3

from upstart_greatest_product_sublist import *
import unittest

class MyTestCases(unittest.TestCase):
  def setUp(self):
    self.inputs_to_outputs = {
      (-3, ): [-3],
      (-3, -4, -5): [-4, -5],
      (-3, -4, 0, -5): [-3, -4],
      (0, ): [0],
      (0, 0, 0): [0],
      (0, 1, 0): [1],
      (1, 2, 3, 0, 4, 5, 6): [4, 5, 6],
      (-4, 5, 6, -7): [-4, 5, 6, -7],
      (-3, 4, -5, 6, -7): [4, -5, 6, -7],
      (-3, 4, 0, 5, 6, -7, -8, 9, 0, 1, -4): [5, 6, -7, -8, 9],
      (-3, -5): [-3, -5],
      (-3, 0, -5): [-3, 0], # hmm... [-3, 0] and [0, -5] are both solutions here; let's say we just return the first of the longest lists
      (5, 0, 3, 4, -3, 5, 6, -7, 1, 5, -7, 8, 7, 0, 2, 5, 6): [5, 6, -7, 1, 5, -7, 8, 7],
      (5, 0, 3, 40, -3, 5, 6, -7, 1, 5, -7, 8, 7, 0, 2, 5, 6): [3, 40, -3, 5, 6, -7, 1, 5],
      (-1, -2, -3, -4, -5): [-2, -3, -4, -5],
      (-1, 2, -3, -4, -5, -6): [2, -3, -4, -5, -6],
      (-1, 2, -3, -4, -5): [-1, 2, -3, -4, -5],
    }
    pass

  def tearDown(self):
    # Delete instances of the class or of an input_to_output array, if required.
    pass

  def test_greatest_product_sublist(self):
    for (input_list, output_list) in self.inputs_to_outputs.items():
      self.assertEqual(greatest_product_sublist(input_list), output_list)

if __name__ == '__main__':
  unittest.main()