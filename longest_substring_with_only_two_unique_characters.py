#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", help="the character string you want to search (to identify the longest substring containing exactly two unique characters)", type=str)
args = parser.parse_args()

'''
General Strategy (no discussion of edge-case handling):
- index1 tracks the beginning of a potential matching string
- index tracks the end of that potential matching string
- within that potential string, index2 tracks the first of a trailing set of repeating characters
- char1 and char2 track the two characters of the substring under consideration. (Note that while char1 always corresponds to index1, char2 does not necessarily correspond to index2, since the trailing set of repeating characters might be a set of char1s.)
- longest is a list of solutions (since there can be more than one)

1. We start out with index1 being at the beginning of the input string, and initialize a potential solution set with just the substring of that first character.
2. We then initialize index2 with the location of first character in the string that doesn't match that first character. (Note that this satisfies our definition for index2 above.)
3. We then initialize index = index2 and start our while loop that increments index through the length of the input string:
  3.a. If the character at index is one of char1 or char2, we have a new potentially longest string.
    3.a.i. If it's longer than what we currently have in the solutions list, replace it with a new list of just this solution.
    3.a.ii. If it's the same length as something in the solutions list, append it.
  3.b. But if the character at index is not one of our current two characters, we need to recalibrate our search:
    (See special case handling below, #5, which comes before what immediately follows here.)
    3.b.i. index1 now has to start at the beggining of the trailing repeating sequence of the last character before the one at index. By definition, this is index2.
    3.b.ii. char1 is now whatever that character made up that trailing repeating sequence.
    3.b.iii. char2 is now the new character at index that didn't match char1 or char2 before.
4. Now, we do the accounting for index2: if our character at index is not the same as the previous character, index2 needs to be updated to index. This way, once the end of a potential solution substring stops repeating, index2 moves on to the next possibly repeating trailing end. This is what prevents index from having to backtrack, since any new solution would obviously want to include all of the repeating characters that were at the end of the previous potential solution in the beginning of the next one under consideration.
5. Finally, we have to handle a special case. Notice a situation where the end of the input string is a single non-repeating character. It could be at the end of a matching substring of the form "abbc". "abb" is already in the solution list, and we know that "bbc" should also be in this list. But when our while loop gets to the end, it's a new character, so the solution-checking logic isn't triggered. But this would only happen at the end, so we can do this check once, where we're examing the potential solution substring that starts with index2 before it is potentially reassigned.
'''

if len(args.input) > 0:
  # the first unique character is the first character
  index1  = 0
  char1   = args.input[0]

  # let's also initialize the solutions list with the trivial solution
  longest = [args.input[0]]

  # Find the (first instance of the) second unique character:
  for charindex, char in enumerate(args.input):
    if char != char1:
      index2 = charindex
      char2  = char
      break

  index = index2

  while index < len(args.input):
    if args.input[index] == char1 or args.input[index] == char2:
      if len(args.input[index1:index+1]) > len(longest[0]):
        longest = [args.input[index1:index+1]]
      elif len(args.input[index1:index+1]) == len(longest[0]):
        longest.append(args.input[index1:index+1])
    else:
      # special case handling
      if index == len(args.input) - 1 and (len(args.input[index2:index+1]) == len(longest[0])):
        longest.append(args.input[index2:index+1])

      index1 = index2
      char1 = args.input[index1]
      char2 = args.input[index]
      
    if args.input[index] != args.input[index-1]:
      index2 = index

    index += 1

  print(longest)
else:
  print("Error: input must have a length of at least 1")