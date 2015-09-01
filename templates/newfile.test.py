#!/usr/bin/env python3

from newfile import *
import unittest

class MyTestCases(unittest.TestCase):
  def setUp(self):
    # Create instances of the class or of an input_to_output array, if required.
    pass

  def tearDown(self):
    # Delete instances of the class or of an input_to_output array, if required.
    pass

  def test_1(self):
    # This is where we might put in the self.assertEqual(value1, value2) statements. Maybe in a for loop, depending on how the tests are set up.
    pass

  def test_2(self):
    # This is where we might put in the self.assertEqual(value1, value2) statements. Maybe in a for loop, depending on how the tests are set up.
    pass

if __name__ == '__main__':
  unittest.main()