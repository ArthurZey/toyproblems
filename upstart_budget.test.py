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

  '''
  def test_parse_args(self):
    self.assertEqual(self.budget.parse_args().income, "80,40,70,200,10,70,0,100,90,10")
    self.assertEqual(self.budget.parse_args().goals, "1:0")

  def test_parse_income(self):
    self.assertEqual(self.budget.parse_income(), [80,40,70,200,10,70,0,100,90,10])

  def test_parse_goals(self):
    self.assertEqual(self.budget.parse_goals(), {1:0})
  '''
  def test_compute_budget(self):
    solutions = [
      [60,60,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75],
      [500/3, 500/3, 500/3, 500],
      [550,550,1450,1450],
      [500,500,500,500],
      [0,0,1000,1000],
      [100,150,150,500],
      [1004/3,1004/3,1004/3,1004],
      [251,251,251,251],
      [1,1,1,1001],
    ]
    for (i, budget) in enumerate(self.budgets):
      self.assertEqual(budget.compute_budget(), [round(float(x), 10) for x in solutions[i]])


class ComplexBudgetTestCase(unittest.TestCase):
  def setUp(self):
    #self.budget = Budget(["500,500,500", "3:900"])
    pass

  def tearDown(self):
    #self.budget = None
    pass

  def test_parse_args(self):
    #self.assertEqual(self.budget.parse_args().income, "500,500,500")
    #self.assertEqual(self.budget.parse_args().goals, "3:900")
    pass
    '''
    args = Budget.parse_args(["some kind of income string", "some kind of goals string"])
    self.assertEqual(args.income, "some kind of income string")
    self.assertEqual(args.goals, "some kind of goals string")
    self.assertEqual(args.tolerance, None)

    args = Budget.parse_args(["-t", "1234", "income", "goals"])
    self.assertEqual(args.income, "income")
    self.assertEqual(args.goals, "goals")
    self.assertEqual(args.tolerance, 1234)
    '''

  def test_parse_income(self):
    #self.assertEqual(self.budget.parse_income(), [500, 500, 500])
    pass
    '''
    self.assertEqual(
      Budget.parse_income("85000,110000,120000,131000,133000,155000,160000,295000,295000,350000"),
      [85000,110000,120000,131000,133000,155000,160000,295000,295000,350000]
      )

    # more tests of variously formated inputs?
    '''

  def test_parse_goals(self):
    #self.assertEqual(self.budget.parse_goals(),{3:900})
    pass
    '''
    self.assertEqual(
      Budget.parse_goals("1:500,4:8472,4:1701,10:100000"),
      {1:500, 4:10173, 10:100000}
      )

    # more tests of variously formated inputs?
    '''

  def test_compute_budget(self):
    #self.assertEqual(self.budget.compute_budget(), {1:200, 2:200, 3:200})
    pass
    '''
    self.assertEqual(
      Budget.create_budget([500, 500, 500], {3:900}, 0),
      {1:200, 2:200, 3:200}
      )
    '''


if __name__ == '__main__':
  unittest.main()