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


''' Test cases:
6 2 2 4 5 => 10

2 3 6 4 2 5

2 0 4 1 2 3 => 5

Approaches:
1. finding local maxima
2. zeroing out