# Copyright (c) 2012-2014 Kapiche Limited
# Author: Ryan Stuart <ryan@kapiche.com>
"""
Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits! But instead of following the Fibonacci sequence
like all good rabbits  do, the zombit population changes according to this bizarre formula, where R(n) is the number of
zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program with only one zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman, a bunch of Professor Boolean's minions passed the time by playing
a guessing game: when will the zombit population be equal to a certain amount? Then, some clever minion objected that
this was too easy, and proposed a slightly different game: when is the last time that the zombit population will be
equal to a certain amount? And thus, much fun was had, and much merry was made.

(Not in this story: Professor Boolean later downsizes his operation, and you can guess what happens to these minions.)

Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n
such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None". S
will be a positive integer no greater than 10^25.
"""
r = {0: 1, 1: 1, 2: 2}  # Store R(n) values


def R(count):
    """Work backwards to compute R(n)."""
    if count not in r:
        n = count // 2
        if count == 2 * n:
            r[count] = R(n) + R(n + 1) + n
        else:
            r[count] = R(n - 1) + R(n) + 1
    return r[count]


def binary_search(space, zombits):
    start, end = 0, zombits
    while start <= end:
        mid = (start + end) // 2
        probe = R(space(mid))
        if probe == zombits:
            return mid
        if probe < zombits:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def answer(zombits):
    zombits = int(zombits, 10)
    bs_even = binary_search(lambda n: n * 2, zombits) * 2
    bs_odd = binary_search(lambda n: n * 2 + 1, zombits) * 2 + 1
    if bs_even < 0:
        answer = None if bs_odd < 0 else bs_odd
    elif bs_odd < 0:
        answer = bs_even
    else:
        answer = max(bs_even, bs_odd)
    return '{}'.format(answer)


if __name__ == '__main__':
    print answer(str(10**25))
