#! /usr/bin/env python3.

# euler_1.py: Finds the sum of all multiples of 3 and 5 under 1000

def multiples(num,lim):
    sum = 0
    for i in range(lim):
        if i % num == 0:
            sum += i
    return sum

result = multiples(3,1000) + multiples(5,1000) - multiples(15,1000)

print(result)