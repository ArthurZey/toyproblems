#!/usr/bin/env python3

from sorting_algorithms import *
import unittest

class SortTests(unittest.TestCase):
  def setUp(self):
    self.inputs_to_outputs = {
      (6, 3, 8, -3, 4, 7, 0, 1, 2, 6, 9, 14): [-3, 0, 1, 2, 3, 4, 6, 6, 7, 8, 9, 14],
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
    # This is where we might put in the self.assertEqual(value1, value2) statements. Maybe in a for loop, depending on how the tests are set up.
    for (input_list, output_list) in self.inputs_to_outputs.items():
      self.assertEqual(insertion_sort(input_list), output_list)

  def test_bubble_sort(self):
    for (input_list, output_list) in self.inputs_to_outputs.items():
      self.assertEqual(bubble_sort(input_list), output_list)

if __name__ == '__main__':
  unittest.main()