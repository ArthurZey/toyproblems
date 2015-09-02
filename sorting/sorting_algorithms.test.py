#!/usr/bin/env python3

from sorting_algorithms import *
import unittest

class SortTests(unittest.TestCase):
  def setUp(self):
    self.inputs_to_outputs = {
      (6, 3, 8, -3, 4, 7, 0, 1, 2, 6, 9, 14): [-3, 0, 1, 2, 3, 4, 6, 6, 7, 8, 9, 14],
      (3, 2, 1): [1, 2, 3],
      (170, 45, 75, 90, 802, 2, 24, 66): [2, 24, 45, 66, 75, 90, 170, 802],
    }

  def tearDown(self):
    self.inputs_to_outputs = None

  def test_parse_input_string(self):
    inputs_to_outputs = {
      "1, 2, 3": [1, 2, 3],
      "6, 3, 8, -3, 4, 7, 0, 1, 2, 6, 9, 14": [6, 3, 8, -3, 4, 7, 0, 1, 2, 6, 9, 14],
    }

    for (input_string, output_list) in inputs_to_outputs.items():
      self.assertEqual(parse_input_string(input_string), output_list)

  def test_insertion_sort(self):
    for (input_list, output_list) in self.inputs_to_outputs.items():
      self.assertEqual(insertion_sort(input_list), output_list)

  def test_bubble_sort(self):
    for (input_list, output_list) in self.inputs_to_outputs.items():
      self.assertEqual(bubble_sort(input_list), output_list)

  def test_merge_sort(self):
    for (input_list, output_list) in self.inputs_to_outputs.items():
      self.assertEqual(merge_sort(input_list), output_list)

  def test_bucket_sort(self):
    for (input_list, output_list) in self.inputs_to_outputs.items():
      for i in range(2, 10):
        self.assertEqual(bucket_sort(input_list, i), output_list)

  def test_radix_lsd_sort(self):
    for (input_list, output_list) in self.inputs_to_outputs.items():
      self.assertEqual(radix_lsd_sort(input_list), output_list)



if __name__ == '__main__':
  unittest.main()