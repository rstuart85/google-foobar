# Copyright (c) 2012-2014 Kapiche Limited
# Author: Ryan Stuart <ryan@kapiche.com>
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
