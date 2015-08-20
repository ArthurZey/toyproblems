#!/usr/bin/env python3

from upstart_budget import *
import unittest

class BudgetTestCases(unittest.TestCase):
  def setUp(self):
    self.incomes = [
      [80,40,70,200,10,70,0,100,90,10],
      [500,0,0,500],
      [1000,100,2000,900],
      [1000,1000,0,0],
      [0,0,1000,1000],
      [100,300,0,500],
      [1001,0,3,1004],
      [1001,0,3,0],
      [3,0,0,1001],
    ]
    # self.goals...we'll test this soon

    self.budgets = list()
    for x in range(0, len(self.incomes)):
      self.budgets.append(Budget([",".join([str(n) for n in self.incomes[x]]), "1:0"]))

  def tearDown(self):
    self.budgets = None

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
    }
    for (input_string, output_list) in inputs_to_outputs.items():
      self.assertEqual(Budget.parse_goals(None, input_string, input_string.count(":")), output_list)
  
  def test_distribute_income(self):
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
      self.assertEqual(Budget.distribute_income(None, input_incomes), [round(float(x), 10) for x in output_distribution])


if __name__ == '__main__':
  unittest.main()