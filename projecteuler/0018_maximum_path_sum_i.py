#!/usr/bin/env python

'''
https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

      *3
    *7   4
   2  *4   6
 8   5  *9   3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                            75
                          95  64
                        17  47  82
                      18  35  87  10
                    20  04  82  47  65
                  19  01  23  75  03  34
                88  02  77  73  07  63  67
              99  65  04  28  06  16  70  92
            41  41  26  56  83  40  80  70  33
          41  48  72  33  47  32  37  16  94  29
        53  71  44  65  25  43  91  52  97  51  14
      70  11  33  28  77  73  17  78  39  68  17  57
    91  71  52  38  17  14  91  43  58  50  27  29  48
  63  66  04  68  89  53  67  30  73  16  69  87  40  31
04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67 (https://projecteuler.net/problem=18), is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

triangle = [
  [75],
  [95, 64],
  [17, 47, 82],
  [18, 35, 87, 10],
  [20,  4, 82, 47, 65],
  [19,  1, 23, 75,  3, 34],
  [88,  2, 77, 73,  7, 63, 67],
  [99, 65,  4, 28,  6, 16, 70, 92],
  [41, 41, 26, 56, 83, 40, 80, 70, 33],
  [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
  [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
  [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
  [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
  [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
  [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]

class GraphNode(object):
  def __init__(self, val):
    self.val = val
    self.children = []
    self.parents = []
    self.max_child_sum = None

  def add_parent(self, parent):
    self.parents.append(parent)
    parent.children.append(self)
    return parent

  def get_max_child_sum(self):
    if self.max_child_sum is not None:
      return self.max_child_sum
    elif len(self.children) == 0:
      self.max_child_sum = self.val
      return self.max_child_sum
    else:
      maxval = None
      for child in self.children:
        child_max = child.get_max_child_sum()
        if maxval is None:
          maxval = self.val + child_max
        else:
          maxval = self.val + child_max if self.val + child_max > maxval else maxval
      self.max_child_sum = maxval
      return self.max_child_sum

for row_num, row in enumerate(triangle):
  for i, item in enumerate(row):
    row[i] = GraphNode(item)
    # add parents, if any
    if row_num > 0:
      if i < len(row) - 1:
        row[i].add_parent(triangle[row_num-1][i])
      if i > 0:
        row[i].add_parent(triangle[row_num-1][i-1])

print(triangle[0][0].get_max_child_sum())