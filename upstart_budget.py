#!/usr/bin/env python3

'''
Introduction
============

Imagine that you were building an application that helps people with their budgeting. Specifically, you want to help people calculate how much they can afford to spend each year, and still meet their longer term financial goals (e.g. buying a house).

Inputs
======

1. The user tells you the income they expect to earn each year for the next N years. Income can be as low as $0, and can vary year to year.

2. The user tells you all the financial goals they have for the next N years. An example of a financial goal is: “I’d like to buy a house in 10 years costing $100,000.” Some years can have no financial goals.

Objective
=========

Your application should tell the user how much money to spend in each year for the next N years. It should choose these amounts with the following considerations:

1. The user’s top priority is to meet all of his or her goals. If this isn’t possible, the program can just return an error.

2. If the user can meet all of his or her goals, they would like to be as happy as possible.

  a. Their happiness is a function of their discretionary spending. The more they spend, the happier they are!

  b. The user experiences declining marginal utility with respect to spending in a particular year. In other words, the first $100 spent in a year gives them more happiness than the second $100, which gives them more happiness than the third $100, and so on. This means the user would prefer to spend their discretionary dollars as evenly as possible across years.

Question
========

Come up with an algorithm that will achieve the objective above. Your solution can be in “psuedo­code”, real code, English precise enough to be like code, a spreadsheet, or whatever other way you feel best allows you to express the solution. Please explain your solution clearly ­“just execute the code, it works” is not a good answer.

Notes
=====

* You don’t need to worry about the user’s expectations of income being wrong, them losing their job, etc.

* Assume no loans, no interest on savings, etc.
'''

import argparse
import sys
from statistics import mean

class Budget:
  def __init__(self, args):
    self.args        = args
    self.parsed_args = self.parse_args()
    self.incomes     = self.parse_income()
    self.goals       = self.parse_goals()


  def parse_args(self):
    parser = argparse.ArgumentParser()
    parser.add_argument("income", help="a quotation-enclosed, comma-separated list of expected net income (whole dollars) for each of the next N years;\nfor example: \"85000,110000,120000,131000,133000,155000,160000,295000,295000,350000\"\nNote that non-numeric characters will be stripped, so \"34k8\" will be interpreted as \"348\".", type=str)
    parser.add_argument("goals", help="a quotation-enclosed, comma-separated list of year-to-goal associations (where years are 1-indexed and not beyond the years specified in the \"income\" parameter);\nfor example: \"1:500,4:8472,4:1701,10:100000\"\nNote that non-numeric characters will be stripped, so \"34k8\" will be interpreted as \"348\".", type=str)
    return parser.parse_args(self.args)

  def parse_income(self):
    return [float(x.strip()) for x in "".join([c for c in self.parsed_args.income if c in "0123456789,"]).split(",")]

  def parse_goals(self):
    result = dict()
    goals_list = [x.strip() for x in "".join([c for c in self.parsed_args.goals if c in "0123456789,:"]).split(",")]
    for x in goals_list:
      year_goal = [float(y.strip()) for y in x.split(":")]
      if year_goal[0] in result:
        result[year_goal[0]] += year_goal[1]
      else:
        result[year_goal[0]] = year_goal[1]
    return result

  def compute_budget(self):
    budget = self.incomes
    for i in range(len(budget) - 1, 0, -1):
      average = mean(budget[:(i+1)])
      if budget[i] < average:
        j = i - 1
        while budget[i] < average and j >= 0:
          if budget[j] > average:
            delta_j = budget[j] - average
            if delta_j > average - budget[i]:
              budget[j] -= average - budget[i]
              budget[i] = average
            else:
              budget[i] += delta_j
              budget[j] = average
          j -= 1
      elif i < len(budget) - 1 and budget[i] > budget[i+1]:
        # need to find the next index that budget[i] is smaller than
        j = i + 1
        while j < len(budget) and budget[i] > budget[j]:
          j += 1
        average = mean(budget[i:j])
        for k in range(i, j):
          budget[k] = average

    return [round(x, 10) for x in budget]


def main():
  the_budget = Budget(sys.argv[1:])
  print(the_budget.compute_budget())
  #parser = parse_args(sys.argv[1:])


if __name__ == '__main__':
  main()