#! /usr/bin/env python3.

# euler_2.py: Finds the sum of all even fibonacci numbers
#             less than 4 million

a = 1
b = 2
fib = 0
sum = 0

limit = input("Find sum of all even fibonacci numbers less than: ")
while fib < limit:
    fib = a + b
    if fib % 2 and fib < limit:
        sum += fib
    a = b
    b = fib

print("The sum of all even fibonacci numbers is %d" % sum)