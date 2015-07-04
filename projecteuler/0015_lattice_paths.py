#!/usr/bin/env python

'''
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

._._.  ._. .  ._. .  . . .  . . .  . . . 
. . |  . |_.  . | .  |_._.  |_. .  | . . 
. . |  . . |  . |_.  . . |  . |_.  |_._. 

How many such routes are there through a 20×20 grid?
'''

# we need to think about this recursively:

# first, look at each of the points on the right and lower edge of the 2x2 grid:
# note that there is only 1 way to get to the far upper-right and lower-left,
# 3 ways to get to the middle-right and middle-bottom, and 6 ways to the bottom-right.

# if we expand this to a 3x3 grid, we just need to build on what we know for a 2x2 grid:
# the number of ways to get to each vertex along the right (top-to-bottom) is 1, 4, 10, 20
# (same goes for the bottom, left-to-right)

# observe also, that the number of ways to get to a specific vertex is the sum of the number of ways
# to get to the vertex above it and the number of ways to get to the vertext to its left

def num_ways_to_right_side_vertices(n):
  # base case
  if n == 2:
    return [1, 3, 6]

  # recursive step that gets the number of ways to get the each of the verticies along the right side
  one_smaller = num_ways_to_right_side_vertices(n-1)

  # initialize the list that holds the number of ways to get to each of the verticies for this n
  this_one = [1]

  # the next veriticies, up to the second-to-last one (n-1), serve as the basis with this_one
  # for the next value in this_one
  for i in range(1, n):
    this_one.append(this_one[-1] + one_smaller[i])

  # finally, because of symmetry, the last element in the list is just twice the previous element
  this_one.append(2*this_one[-1])

  return this_one

print(num_ways_to_right_side_vertices(20)[-1])
