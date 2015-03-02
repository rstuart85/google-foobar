# Copyright (c) 2012-2014 Kapiche Limited
# Author: Ryan Stuart <ryan@kapiche.com>
"""
Peculiar balance
================

Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an
obstacle. The  door will only open if a challenge is solved correctly. The future of the zombified rabbit population is
at stake, so Beta reads the  challenge: There is a scale with an object on the left-hand side, whose mass is given in
some number of units. Predictably, the task is to  balance the two sides. But there is a catch: You only have this
peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one  for each power of 3. Being a brilliant
mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced  exactly using this set.

To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the
weights should be  placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.

The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight,
and so on. Each  string is one of:

"L" : put weight on left-hand side
"R" : put weight on right-hand side
"-" : do not use weight

To ensure that the output is the smallest possible, the last element of the list must not be "-".

x will always be a positive integer, no larger than 1000000000.
"""
from itertools import takewhile, count
import sys


def answer(x):
    i = tuple(takewhile(lambda z: z / 3 < x, (3 ** n for n in count(0))))
    j = tuple(sum(i[:n]) for n in range(len(i)))
    c = len(i) - 1
    side = 'R'
    result = ["-"] * len(i)
    while x:
        if x >= i[c]:
            x -= i[c]
            result[c] = side
        elif x >= i[c] - j[c]:
            x = i[c] - x
            result[c] = side
            side = 'R' if side == 'L' else 'L'
        c -= 1
    if result and result[-1] == '-':
        del result[-1]
    return result

if __name__ == "__main__":
    for x in (int(n, 10) for n in sys.argv[1:]):
        print answer(x)
