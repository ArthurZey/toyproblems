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
    self.parsed_args = self.parse_args(args)
    self.incomes     = self.parse_incomes(self.parsed_args.incomes)
    self.goals       = self.parse_goals(self.parsed_args.goals)


  def parse_args(self, args):
    '''Parse arguments into variables readily available to the class for further processing; provides built-in niceties for calling the script from the command line.'''

    parser = argparse.ArgumentParser()
    parser.add_argument("incomes", help="a quotation-enclosed, comma-separated list of expected net income (whole dollars) for each of the next N years;\nfor example: \"85000,110000,120000,131000,133000,155000,160000,295000,295000,350000\"\nNote that non-numeric characters will be stripped, so \"34k8\" will be interpreted as \"348\".", type=str)
    parser.add_argument("goals", help="a quotation-enclosed, comma-separated list of year-to-goal associations (where years are 1-indexed and not beyond the years specified in the \"income\" parameter);\nfor example: \"1:500,4:8472,4:1701,10:100000\"\nNote that non-numeric characters will be stripped, so \"34k8\" will be interpreted as \"348\".", type=str)
    return parser.parse_args(args)

  def parse_incomes(self, incomes_string):
    '''Parse (and sanitize) a string of year-by-year incomes into a list of floating-point values.'''

    return [float(x.strip()) for x in "".join([c for c in incomes_string if c in "0123456789,"]).split(",")]

  def parse_goals(self, goals_string):
    '''Parse (and sanitize) a string of year:dollar goals into a list of year-by-year goals, with multiple goals for a given year combined.

      Presupposes that incomes have already been parsed into self.incomes.'''

    # Create an empty list for each year: If this is being called within an actual class instantiation, use len(self.incomes). Otherwise, use the number of colons in the input string as an upper bound.
    result = [0 for x in [c for c in goals_string if c == ":"]] if self is None else [0 for x in self.incomes]
    for year_to_goal_string in [x.strip() for x in "".join([c for c in goals_string if c in "0123456789,:"]).split(",")]:
      result[int(year_to_goal_string.split(":")[0].strip())-1] += float(year_to_goal_string.split(":")[1].strip())

    return result

  def distribute_income(self, incomes):
    '''Take in list of incomes for consecutive years, and return a distribution of the optimal spending over those years, assuming no particular spending requirements/goals in any year. Optimal spending means minimizing the decreasing marginal utility of each additional dollar spent. I believe this can also be thought of as minimizing the standard deviation.

    General strategy:
    0. Key observation that's relevant to the consideration of the mathematics and algorithm design: The optimal spending will be monotonically increasing, year-over-year.
    1. Start at the last year (and move backward).
    2. For any given year, calculate the average of all the years leading up to and including it.
      a. If the the income in that year is below that average, reallocate income from the nearest previous year that's above the average. (Mathematically, it's equivalent to allocate everything from the immediately previous year, even though that might put it under the average or even negative!)
      b. If the income is above the average, but less than the following year (the previously _considered_ year in our algorithm), do nothing.
      c. If the income is above the following year, take the average of those two years and distribute evenly among them. Continue considering the next following year, and if the new average is bigger than that next year, average across all three and distribute evenly. Continue until the average is no longer greater than the next year considered.
    3. Move on to the previous year.
    '''

    # Initialize the distribution with the current given incomes.
    distribution = [float(x) for x in incomes]

    # Start at the end and move backward.
    for year_index in range(len(distribution) - 1, 0, -1):
      # Compute the average income of all the years leading up to the year under consideration.
      average = mean(distribution[:(year_index + 1)])


      if distribution[year_index] < average:
        # Borrow from the previous year the amount necessary to get this year to the average.
        distribution[year_index - 1] -= average - distribution[year_index]

        # Allocate that amount to the current year by just setting it to the average.
        distribution[year_index] = average

      elif year_index < len(distribution) - 1 and distribution[year_index] > distribution[year_index + 1]:
        # We need to keep track of how many years we can distribute over, and we'll be considering them one by one. We should be treating all consecutive years together (since that's how we might reason about it on paper), but because of how averaging works, we'll end up with a mathematically equivalent result.
        j = year_index + 1

        # Look over (and potentially distribute to) all the following years where this year's distribution (which is modified "in place") is greater than that year.
        while j < len(distribution) and distribution[year_index] > distribution[j]:
          # Replace all the values between year_index and j with the average of all the values between year_index and j.
          average = mean(distribution[year_index:j+1])
          for k in range(year_index, j+1):
            distribution[k] = average

          # Move on to the next year that might need to be distributed to.
          j += 1

    return [round(x, 10) for x in distribution]

def main():
  the_budget = Budget(sys.argv[1:])
  print(the_budget.compute_budget())
  #parser = parse_args(sys.argv[1:])


if __name__ == '__main__':
  main()