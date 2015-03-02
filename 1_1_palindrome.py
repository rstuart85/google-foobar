# Copyright (c) 2012-2014 Kapiche Limited
# Author: Ryan Stuart <ryan@kapiche.com>
"""
Palindrome
==========

To help Beta Rabbit crack the lock, write a function answer(n) which returns the
smallest positive integer base b, at least 2, in which the integer n is a
palindrome. The input n will satisfy "0 <= n <= 1000".

Test cases
==========

Inputs:
    (int) n = 0
Output:
    (int) 2

Inputs:
    (int) n = 42
Output:
    (int) 4
Given a number n, return a base b where the number represented in that base is a palindrome.
"""
import string
import sys


def int_to_base(num, b, numerals=string.digits + string.lowercase + string.uppercase):
        return ((num == 0) and numerals[0]) or (int_to_base(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def answer(n):
    def bases(num):
        start = 2
        while True:
            yield (start, int_to_base(num, start))
            start += 1
    for base, repr in bases(n):
        if repr == repr[::-1]:
            return base


if __name__ == '__main__':
    print answer(int(sys.argv[1]))
