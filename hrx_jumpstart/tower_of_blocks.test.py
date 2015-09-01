#!/usr/bin/env python3

from tower_of_blocks import *
import unittest

class TowerOfBlockTestCases(unittest.TestCase):
  def setUp(self):
    self.inputs_to_outputs = {
      (6,2,2,4,5): 7,
      (2,0,4,1,2,3): 5,
      (2,3,6,4,2,5): 4,
      (1,3,0,3): 3,
      (7,1,2,3,4,5): 10,
      (2,1,6,1,4,1,2,1,3): 9,
      (2,1,3,1,4,1): 3,
      (1,2,3,4,5): 0,
      (2,1,3,4): 1,
      (2,2,1,2): 1,
      (2,1,2,2,3): 1,
      (5,4,1,1,1,4): 9,
    }

  def tearDown(self):
    self.inputs_to_outputs = None

  def test_solve_via_finding_local_maxima(self):
    for (input_blocks, output_water) in self.inputs_to_outputs.items():
      self.assertEqual(tower1(input_blocks), output_water)
  '''
  def test_solve_via_zeroing_out(self):
    for (input_blocks, output_water) in self.inputs_to_outputs.items():
      self.assertEqual(tower2(input_blocks), output_water)
  '''

  def test_solve_via_max_bounds_at_each_index(self):
    for (input_blocks, output_water) in self.inputs_to_outputs.items():
      self.assertEqual(tower3(input_blocks), output_water)

if __name__ == '__main__':
  unittest.main()