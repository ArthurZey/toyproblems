Assignment
==========

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

  1. Their happiness is a function of their discretionary spending. The more they spend, the happier they are!

  2. The user experiences declining marginal utility with respect to spending in a particular year. In other words, the first $100 spent in a year gives them more happiness than the second $100, which gives them more happiness than the third $100, and so on. This means the user would prefer to spend their discretionary dollars as evenly as possible across years.

Question
--------

Come up with an algorithm that will achieve the objective above. Your solution can be in “psuedo­code”, real code, English precise enough to be like code, a spreadsheet, or whatever other way you feel best allows you to express the solution. Please explain your solution clearly ­“just execute the code, it works” is not a good answer.

Notes
-----

* You don’t need to worry about the user’s expectations of income being wrong, them losing their job, etc.

* Assume no loans, no interest on savings, etc.


Solution
========

Preliminary note: At the time of doing this problem, I have about 1-2 weeks' worth of Python programming experience.

Assumptions
-----------
In addition to the stated assumptions:

1. The universe ends after the last year for which income data is provided: If goals are specified past that year, the program gracefully quits, since it is impossible to know whether the user made an error, expected zero income in unspecified years, expected a continuation of the last specified year's income, or expected some kind of extrapolation of income trajectory based on curve-fitting.
2. Inputs are all positive floating-point numbers.
3. All non-numeric, non-separators are stripped from the inputs without returning any errors or warnings. (They are assumed to be typos.)
4. Precision is limited to 10 decimal places during calculation, then rounded to 2 for display purposes.

In General
----------
1. Verify that the goals are achievable.
2. Adjust the "income" of each year by subtracting the goals from the income in the years they must ultimately be achieved.
  * It's okay if we end up with negative numbers here: Since we have have already verified that the goals are achievable, we know that we will be able to distribute previous years' income "forward" (i.e., later in time).
3. Using the previous step's "goal-adjusted income", reallocate "savings" from previous years to future years in a way that minimizes loss of value due to diminishing marginal returns from spending discretionary dollars. (This is the meat of the algorithm!)
  * The key insight here is that *the optimal allocation of discretionary dollars is monotonically increasing*: Since dollars cannot be saved for use in the past, it is not inherently a problem for discretionary spending to be higher in a later year. However, if discretionary spending were greater in an earlier year than a later year, that would immediately signal a problem, since the possibility of saving part of the earlier year's money for use in the later year means that we could reallocate those funds in a way that increases the marginal utility of the dollars spent in the earlier year.

(1) Verification that the goals are achievable & (2) Generating the goal-adjusted income
----------------------------------------------------------------------------------------
We can verify that the goals are achievable as we're generating the goal-adjusted income:

1. Start at the first year (and move forward).
2. For any given year, sum up the (goal-adjusted) incomes for all the prior years.
  1. If that exceeds the goal for the current year under consideration, provide an error message and gracefully exit.
  2. If that does not exceed the goal for the current year under consideration, subtract the goal from the income for the current year.
3. Move on to the following year.

(3) Reallocating money to achieve the optimal discretionary spending distribution
---------------------------------------------------------------------------------
1. Start at the last year (and move backward).
2. For any given year, calculate the average of all the years leading up to and including it.
  1. If the the income in that year is below that average, reallocate income from the nearest previous year that's above the average. (Mathematically, it's equivalent to allocate everything from the immediately previous year, even though that might put it under the average or even make it negative!)
  2. If the income is above the average, but less than the following year (the previously _considered_ year in our algorithm), do nothing.
  3. If the income is above the following year, take the average of those two years and distribute evenly among them. Continue considering the next following year, and if the new average is bigger than that next year, average across all three and distribute evenly. Continue until the average is no longer greater than the next year considered.
3. Move on to the previous year.


Development Approach
====================
1. I decided to wrap this functionality in a `Budget` class. This allows for better modularity and possible inclusion in other code. I regard it as a pretty standard practice. There may have been more efficient ways to develop this class. I wasn't terribly worried about that for this context, since speed of development was a high priority.
2. I stubbed out the various methods I'd have to use (including writing the docstring for each one):
  1. those that parse inputs
  2. one that adjust the incomes by the goals (and verifies that the goals are achievable)
  3. one that distributes incomes/spending in the optimal way
  At this stage, I was not worried about the method that would print out the result in a pretty way.
3. Most importantly, I utilized test-driven development (TDD): For each method that I would implement in the `Budget` class (in `upstart_budget.py`), I would first write a `unittest` in `upstart_budget.test.py` for enough different expected input-output pairs that I was comfortable with my code's functionality. Strictly speaking, I could have written a greater diversity of tests for each method, been more concerned with hitting 100% code coverage, tested my `__init__` and `__str__` class methods, written more integration tests, and used slightly tighter code and more standard implementations of unit testing, but as before, given the need for speedier development, I deprioritized those aspects.
4. When implementing the various methods, I prioritized code readability over strict computational/space efficiency, and I commented heavily throughout. In some cases, I wrote condensed code (lots of method nesting or chaining), simply because it wasn't terribly relevant to the main thrust of the algorithm and it made for fewer lines of code (which would have had its own implications for readability!).
5. Finally, when I was satisfied that my code generated the correct substantive solution, I made sure that the results would be printed out in an easily apprehensible way by adding the `__str__` class method.
5. I wanted to make sure that the script could either be run from the command line with parameters, or called internally via some code. I used the Python3 `argparse` class to facilitate command-line argument parsing in a user-friendly way.


Running the Code
================

I have only tested this on Mac OS and am confident my instructions below work equally well for almost any Linux (*nix) distribution. You'll have to figure out how to run it on Windows or other architectures.

1. Make sure your machine runs Python3. Running the scripts as executables requires that Python3 is available at `/usr/bin/env python3`.
2. Assuming that you have the relevant files on your local machine (either via `git clone`, downloading, or copy-and-pasting), make sure they are executable by running `chmod a+x upstart_budget.*`
3. To execute the tests, from the directory where you have the files, simply run `./upstart_budget_tests.py`
  * You can modify the tests in the file and play around with them yourself. I did not document the code in the test file, but it's easy to extrapolate how to add more test cases.
4. To execute the code, from the directory where you have the files, run `./upstart_budget.py [incomes] [goals]`
  * `[incomes]` is a quotation-mark-enclosed, comma-separated list of incomes for the set of consecutive years over which the program runs. For example: `"85000,110000,120000,131000,133000,155000,160000,295000,295000,350000"`
  * `[goals]` is a quotation-mark-enclosed, comma-separated pairing of year-to-goal associations (using a colon), specifying a year and the financial goal for that year. There can be multiple goals for a given year, and not every year must have a goal. For example: `"1:500,4:8472,4:1701,10:100000"`
  * An example complete call is `./upstart_budget.py "85000,110000,120000,131000,133000,155000,160000,295000,295000,350000" "1:500,4:8472,4:1701,10:100000"`