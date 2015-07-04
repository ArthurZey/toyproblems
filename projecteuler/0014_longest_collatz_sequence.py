#!/usr/bin/env python

'''
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

# let's say that we've already processed the chain 2 → 1
# let's keep a dictionary / hash table that maps the number to the number of steps to get to 1
terminates_at_1 = {2: 2}
longest_chain_length = 2

for n in range(3, 1000000):
  # build up the chain
  chain = list()
  step = n
  # we only need to create the chain up to the point where we get to a number that we already know
  # terminates at 1
  while step not in terminates_at_1:
    # add the step to the chain
    chain.append(step)
    # "increement" the step to the next value in the sequence
    step = int(step/2) if step%2 == 0 else int(3*step + 1)

  # once we're out of the loop, we've built up chain to contain all the values that will ultimately terminate at 1. let's process them now:
  for i, number in enumerate(chain):
    # for each number in chain (which is unique), we know how many iterations it takes to get to 1;
    # namely, the number of steps for the last step (which is what we got when we got dumped out of
    # the while loop above), and how many more numbers are in the chain we created:
    terminates_at_1[number] = terminates_at_1[step] + len(chain) - i

# now we need the largest value out of terminates_at_1
print(max(terminates_at_1, key=terminates_at_1.get))
