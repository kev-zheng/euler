#! /usr/bin/env python3.

# euler_5.py: Finds smallest number divisible by
#             numbers 1 through 20

from functools import reduce


def gcd(a, b):
    while True:
        rem = a % b
        if rem == 0:
            return b
        a = b
        b = rem


def lcm(a, b):
    return (a * b) / gcd(a,b)

# iteratively compute least common multiple
print(reduce(lcm,range(1,21)))
