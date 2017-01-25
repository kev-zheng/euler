#! /usr/bin/env python3.

a = 1
b = 2
fib = 0
sum = 0
while(fib < 4000000):
    fib = a + b
    if fib % 2 and fib < 4000000:
        sum += fib
    a = b
    b = fib

print(sum)