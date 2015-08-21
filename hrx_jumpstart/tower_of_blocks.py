#!/usr/bin/env python3

'''
The Tower of Blocks Puzzle
==========================

Before we start
---------------
This is a tricky problem, and it’s very visual. We might not get to do much pseudocode, and we almost certainly won’t write a full solution. Your ability to represent the problem on the whiteboard in different ways, and to move back and forth between them, will be crucially important.

Prompt
------
Suppose we have a bunch of wooden blocks. Each block is the same width and height, and they’re arranged in a row of vertical stacks to make a little 2-dimensional tower:

  █
  █  █
█ █ ██
█ ████ 

We’re going to take a hose and spray water all over the top of our tower, so water comes down across the top. The water drains off to the sides of the tower (but not out the bottom), so the result is that water pools anywhere there is a depression:

⇣ ⇣ ⇣ ⇣ ⇣
    █
    █▓▓█
  █▓█▓██
↵ █▓████ ↳

We want to find out, given an arbitrary tower of blocks, how many “blocks of water” will it hold? (In this case, 5.)

  █
  █▓▓█
█▓█▓██
█▓████
204123 -> 5

When asked, offer the alternate representation of a list of numbers of blocks in each stack. We put in the array, we get out 5. That’s about as much context as you should give them.

For our purposes, there is no complexity requirement. Finding a naive solution first, and possibly optimizing, is expected.

The trick here is that we’re giving the students two representations of the same thing: A visual metaphor of a tower of blocks, and an array of integers with an expected output. It seems like very little information, but it’s actually a huge start on solving the problem. Manipulating these representations, generating them, and moving between them is crucial. Most students should be able to attack it from any angle and start making progress, and the guidance you provide will mostly be repeated application of the question: “Yeah, that makes sense, but what does that mean over here?”

Your best preparation to give this (or any) question is, of course, to solve it for yourself. There is a fairly obvious algorithm that runs in n^2 time, and a number of optimizations will pull it down into linear time. There is also one particularly elegant linear-time solution that will probably seem obvious in retrospect. You can come back when you’re ready.
'''

import argparse

def tower1(blocks):
  # some cases for 0, 1, 2 columns?

  water = 0
  
  blocks = list(blocks)
  print(blocks)

  index_of_greatest_righthand_local_maximum = None

  for (col_index, col) in enumerate(blocks):
    print(blocks)
    print("considering col " + str(col_index) + ":")

    if index_of_greatest_righthand_local_maximum is not None and (col_index > 0 and col > blocks[col_index-1]):
      # if (there has previously been a righthand local maximum) and (we're on a lefthand local maximum)
      print("  there has previously been a righthand local maximum at index " + str(index_of_greatest_righthand_local_maximum) + " (" + str(blocks[index_of_greatest_righthand_local_maximum]) + ") and we're on a lefthand local maximum")

      if col >= blocks[index_of_greatest_righthand_local_maximum]: 
        # case 1: our lefthand local maximum is equal to or greater
        # go back and fill in with water!
        print("    we're in case 1: our lefthand local maximum (" + str(col) + ") is >= the greatest righthand local maximum (" + str(blocks[index_of_greatest_righthand_local_maximum]) + ")")
        for i in range(index_of_greatest_righthand_local_maximum + 1, col_index):
          print ("      filling index " + str(i) + " with " + str(blocks[index_of_greatest_righthand_local_maximum] - blocks[i]) + " unit(s) of water")
          water += blocks[index_of_greatest_righthand_local_maximum] - blocks[i]
          blocks[i] = blocks[index_of_greatest_righthand_local_maximum]

        # now that we've done this, though, the greatest righthand local maximum is no longer what it was before, so we need to reset. The current column is a candidate for being the greatest righthand column, and that's captured below. So for now, it's safe to just clear it.
        index_of_greatest_righthand_local_maximum = None

      else:
        # case 2: our lefthand local maximum is smaller than
        # we need to backtrack to find the closest predecessor that's equal to or greater than our lefthand local maximum (and by hypothesis, we need not go further back than the index_of_greatest_righthand_local_maximum); moreover, we can fill up as we go along
        print ("    we're in case 2: our lefthand local maximum (" + str(col) + ") is < the greatest righthand local maximum (" + str(blocks[index_of_greatest_righthand_local_maximum]) + ")")
        print ("      backtracking as far back as greatest righthand local maximum (index " + str(index_of_greatest_righthand_local_maximum) + ")")
        for i in range(col_index - 1, index_of_greatest_righthand_local_maximum - 1, -1):
          if blocks[i] < col:
            # we're still searching, but we can fill up
            print ("      " + str(blocks[i]) + " (at index " + str(i) + ") is still smaller than our lefthand local maximum (" + str(col) + ")")
            print ("        filling index " + str(i) + " with " + str(col - blocks[i]) + " unit(s) of water")
            water += col - blocks[i]
            blocks[i] = col
          else:
            # meaning we've found a column in our backtracking that's equal to or greater
            print ("      found a column (value " + str(blocks[i]) + " at index " + str(i) + ") that's >= our lefthand local maximum")
            break
    else:
      # we're not at a lefthand local maximum, so nothing to do
      print("  we're not at a lefthand local maximum, so nothing to do.") 
      pass

    # potentially update index_of_greatest_righthand_local_maximum
    if col_index < len(blocks) - 1 and col > blocks[col_index+1]:
      if index_of_greatest_righthand_local_maximum is None or col > blocks[index_of_greatest_righthand_local_maximum]:
        print ("  current column is new greatest righthand local maximum")
        index_of_greatest_righthand_local_maximum = col_index

  return water

def tower2(blocks):
  return 0

def tower3(blocks):
  # http://stackoverflow.com/questions/24414700/amazon-water-collected-between-towers

def main():
  parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument("blocks", help="a quotation-mark-enclosed, comma-separated list of how many blocks are in each column, from left to right;\n\nFor example: \"6,2,2,4,5\"")
  parsed_args = parser.parse_args()

  blocks = [int(x.strip()) for x in "".join([c for c in parsed_args.blocks if c in "0123456789,"]).split(",")]
  print(blocks)
  
  tower1(blocks)


if __name__ == '__main__':
  main()