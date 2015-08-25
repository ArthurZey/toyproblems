#!/usr/bin/env python3

'''
Introduction
------------

Imagine that you were building an application that helps people with their budgeting. Specifically, you want to help people calculate how much they can afford to spend each year, and still meet their longer term financial goals (e.g. buying a house).

Inputs
------

1. The user tells you the income they expect to earn each year for the next N years. Income can be as low as $0, and can vary year to year.

2. The user tells you all the financial goals they have for the next N years. An example of a financial goal is: “I’d like to buy a house in 10 years costing $100,000.” Some years can have no financial goals.

Objective
---------

Your application should tell the user how much money to spend in each year for the next N years. It should choose these amounts with the following considerations:

1. The user’s top priority is to meet all of his or her goals. If this isn’t possible, the program can just return an error.

2. If the user can meet all of his or her goals, they would like to be as happy as possible.

  a. Their happiness is a function of their discretionary spending. The more they spend, the happier they are!

  b. The user experiences declining marginal utility with respect to spending in a particular year. In other words, the first $100 spent in a year gives them more happiness than the second $100, which gives them more happiness than the third $100, and so on. This means the user would prefer to spend their discretionary dollars as evenly as possible across years.

Question
--------

Come up with an algorithm that will achieve the objective above. Your solution can be in “psuedo­code”, real code, English precise enough to be like code, a spreadsheet, or whatever other way you feel best allows you to express the solution. Please explain your solution clearly ­“just execute the code, it works” is not a good answer.

Notes
-----

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

    more_goals_than_incomes = len(self.goals) - len(self.incomes)
    if more_goals_than_incomes > 0:
      print("Goals may not be specified for years beyond for which there are specified incomes. Consider including " + str(more_goals_than_incomes) + " more year" + ("s" if more_goals_than_incomes != 1 else "") + " of income data.")
      sys.exit(0)

    self.goal_adjusted_incomes = self.adjust_incomes_by_goals(self.incomes, self.goals)

    self.optimal_discretionary_spending = self.distribute_incomes(self.goal_adjusted_incomes)

  def __str__(self):
    '''Display our inputs and outputs in a decently formatted table.'''

    output = ""

    max_len_goals = len(str(max([round(float(x), 2) for x in self.goals])))
    max_len_incomes = len(str(max([round(float(x), 2) for x in self.incomes])))

    header_format = (
      "{:>6}"
      "{:>" + str(max(max_len_goals + 2, 8)) + "}"
      "{:>" + str(max(max_len_incomes + 2, 10)) + "}"
      "{:>" + str(max(max_len_incomes + 2, 25)) + "}"
    )
    row_format = (
      "{:>6}"
      "{:>" + str(max(max_len_goals + 2, 8)) + ".2f}"
      "{:>" + str(max(max_len_incomes + 2, 10)) + ".2f}"
      "{:>" + str(max(max_len_incomes + 2, 25)) + ".2f}"
    )

    output += "\n" + header_format.format(
      "Year",
      "Goals",
      "Incomes",
      "Discretionary Spending"
    )

    for i in range(0, len(self.incomes)):
      output += "\n" + row_format.format(
        (i+1),
        (round(float(self.goals[i]), 2) if i < len(self.goals) else round(float(0), 2)),
        round(float(self.incomes[i]), 2),
        round(float(self.optimal_discretionary_spending[i]), 2)
      )
    return output


  def parse_args(self, args):
    '''Parse arguments into variables readily available to the class for further processing; provides built-in niceties for calling the script from the command line.'''

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("incomes", help="a quotation-mark-enclosed, comma-separated list of expected net income for each of the next N years;\nfor example: \"85000,110000,120000,131000,133000,155000,160000,295000,295000,350000\"\nNote that non-numeric characters will be stripped, so \"34k8\" will be interpreted as \"348\".\n\n", type=str)
    parser.add_argument("goals", help="a quotation-mark-enclosed, comma-separated list of year-to-goal associations (where years are 1-indexed and not beyond the years specified in the \"income\" parameter);\nfor example: \"1:500,4:8472,4:1701,10:100000\"\nNote that non-numeric characters will be stripped, so \"34k8\" will be interpreted as \"348\".\n\n", type=str)
    return parser.parse_args(args)

  def parse_incomes(self, incomes_string):
    '''Parse (and sanitize) a string of year-by-year incomes into a list of floating-point values.'''

    return [float(x.strip()) for x in "".join([c for c in incomes_string if c in "0123456789.,"]).split(",")]

  def parse_goals(self, goals_string):
    '''Parse (and sanitize) a string of year:dollar goals into a list of year-by-year goals, with multiple goals for a given year combined.
    '''

    goals = list()
    
    for year_to_goal_string in [x for x in "".join([c for c in goals_string if c in "0123456789.,:"]).split(",")]:
      
      year = int(year_to_goal_string.split(":")[0])

      goal = float(year_to_goal_string.split(":")[1])
      
      if year > len(goals):
        goals.extend([0] * (year - len(goals)))

        goals[year-1] = goal
      else:
        goals[year-1] += goal
 
    return goals

  def adjust_incomes_by_goals(self, incomes, goals):
    '''Take in the list of incomes and list of goals, and begin to adjust the income numbers by "allocating" that income to goals in the same year. Perform a check as we go on to determine whether all goals are still achievable.

    General strategy:
    0. Key observation that's relevant to this step's being as simple as it is: Given how the distribute_incomes() class method is implemented, it's safe to allow negative incomes as a result of this method in a given year, as discretionary spending will be pulled forward as necessary to result in net non-negative values at the end of the distribute_incomes() method call.
    1. Start at the first year (and move forward).
    2. For any given year, sum up the (goal-adjusted) incomes for all the prior years.
      a. If that exceeds the goal for the current year under consideration, provide an error message and gracefully exit.
      b. If that does not exceed the goal for the current year under consideration, subtract the goal from the income for the current year.
    3. Move on to the following year.
    '''

    goal_adjusted_incomes = [float(x) for x in incomes]

    for year_index in range(len(goals)):

      if sum(goal_adjusted_incomes[:year_index+1]) < goals[year_index]:
        print("Unfortunately, your goals are not achievable. You may consider something less ambitious in at least year " + str(year_index + 1) + ".")
        sys.exit(0)
      else:
        goal_adjusted_incomes[year_index] -= goals[year_index]

    return goal_adjusted_incomes

  def distribute_incomes(self, incomes):
    '''Take in list of incomes (goal-adjusted or not) for consecutive years, and return a distribution of the optimal spending over those years. Optimal spending means minimizing the decreasing marginal utility of each additional dollar spent. I believe this can also be thought of as minimizing the standard deviation.

    General strategy:
    0. Key observation that's relevant to the consideration of the mathematics and algorithm design: The optimal spending will be monotonically increasing, year-over-year.
    1. Start at the last year (and move backward).
    2. For any given year, calculate the average of all the years leading up to and including it.
      a. If the the income in that year is below that average, reallocate income from the nearest previous year that's above the average. (Mathematically, it's equivalent to allocate everything from the immediately previous year, even though that might put it under the average or even make it negative!)
      b. If the income is above the average, but less than the following year (the previously _considered_ year in our algorithm), do nothing.
      c. If the income is above the following year, take the average of those two years and distribute evenly among them. Continue considering the next following year, and if the new average is bigger than that next year, average across all three and distribute evenly. Continue until the average is no longer greater than the next year considered.
    3. Move on to the previous year.
    '''

    distribution = [float(x) for x in incomes]

    for year_index in range(len(distribution) - 1, 0, -1):
      average = mean(distribution[:(year_index + 1)])


      if distribution[year_index] < average:
        distribution[year_index - 1] -= average - distribution[year_index]

        distribution[year_index] = average

      elif year_index < len(distribution) - 1 and distribution[year_index] > distribution[year_index + 1]:
        j = year_index + 1

        while j < len(distribution) and distribution[year_index] > distribution[j]:
          average = mean(distribution[year_index:j+1])
          for k in range(year_index, j+1):
            distribution[k] = average

          j += 1

    return [round(x, 10) for x in distribution]

def main():
  the_budget = Budget(sys.argv[1:])
  print(the_budget)

if __name__ == '__main__':
  main()
