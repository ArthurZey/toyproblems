#!/usr/bin/env python3

from upstart_budget import *
import unittest

class BudgetTestCases(unittest.TestCase):

  def test_parse_args(self):
    inputs_to_outputs = {
      ("80,40,70,200,10,70,0,100,90,10", "1:0"): ["80,40,70,200,10,70,0,100,90,10", "1:0"],
    }
    for (input_args, output_args) in inputs_to_outputs.items():
      self.assertEqual(Budget.parse_args(None, input_args).incomes, output_args[0])
      self.assertEqual(Budget.parse_args(None, input_args).goals, output_args[1])

  def test_parse_incomes(self):
    inputs_to_outputs = {
      "80,40,70,200,10,70,0,100,90,10": [80,40,70,200,10,70,0,100,90,10],
    }
    for (input_string, output_list) in inputs_to_outputs.items():
      self.assertEqual(Budget.parse_incomes(None, input_string), output_list)
  
  def test_parse_goals(self):
    inputs_to_outputs = {
      "1:0": [0],
      "2:5,6:3,7:2,1:2,3:6,2:6,3:1": [2,11,7,0,0,3,2],
    }
    for (input_string, output_list) in inputs_to_outputs.items():
      self.assertEqual(Budget.parse_goals(None, input_string), output_list)
  
  def test_adjust_incomes_by_goals(self):
    inputs_to_outputs = {
      ((10,4,4,9,9),(10,0,4,10)):[0,4,0,-1,9],
    }
    for (input_incomes_and_goals, output_goal_adjusted_incomes) in inputs_to_outputs.items():
      self.assertEqual(Budget.adjust_incomes_by_goals(None, input_incomes_and_goals[0], input_incomes_and_goals[1]), [round(float(x), 10) for x in output_goal_adjusted_incomes])

  def test_distribute_incomes(self):
    inputs_to_outputs = {
      (80,40,70,200,10,70,0,100,90,10):[60,60,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75],
      (500,0,0,500):[500/3, 500/3, 500/3, 500],
      (1000,100,2000,900):[550,550,1450,1450],
      (1000,1000,0,0):[500,500,500,500],
      (0,0,1000,1000):[0,0,1000,1000],
      (100,300,0,500):[100,150,150,500],
      (1001,0,3,1004):[1004/3,1004/3,1004/3,1004],
      (1001,0,3,0):[251,251,251,251],
      (3,0,0,1001):[1,1,1,1001],
      (10,8,8,9,9):[26/3,26/3,26/3,9,9],
      (10,5,5,6,6):[6.4,6.4,6.4,6.4,6.4],
      (10,4,4,9,9):[6,6,6,9,9],
    }
    for (input_incomes, output_distribution) in inputs_to_outputs.items():
      self.assertEqual(Budget.distribute_incomes(None, input_incomes), [round(float(x), 10) for x in output_distribution])

  def test_optimal_discretionary_spending(self):
    inputs_to_outputs = {
      ((10,4,4,9,9),(10,0,4,10)): [0,1,1,1,9],
      ((85000,110000,120000,131000,133000),(0,90000,110000,0,100000)): [115000/3,115000/3,115000/3,82000,82000],
    }
    for (input_incomes_and_goals, output_optimal_discretionary_spending) in inputs_to_outputs.items():
      self.assertEqual(Budget.distribute_incomes(None, Budget.adjust_incomes_by_goals(None, input_incomes_and_goals[0], input_incomes_and_goals[1])), [round(float(x), 10) for x in output_optimal_discretionary_spending])

if __name__ == '__main__':
  unittest.main()