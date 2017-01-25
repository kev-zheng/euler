#! /usr/bin/env python3.

# euler_3.py: Finds largest prime factors

import math


def isprime(n):
    return n > 1 and all(n % i for i in range(2,n))

num = int(input("Find largest prime factor of: "))

max = 0
for i in range(1,int(math.sqrt(num)),2):
    print(i, end='\r')
    if isprime(i) and num % i == 0:
        max = i

print("The greatest common factor of %d is %d" %(num,max))