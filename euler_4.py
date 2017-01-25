#! /usr/bin/env python3.

# euler_4.py: Finds largest palindrome product
#             of 3 digit numbers

def ispalindrome(num):
    return str(num) == str(num)[::-1]

max = 0
i = 999
j = 999
while i > 100:
    j = 990
    while(j > 100):
        num = i * j
        if ispalindrome(num) and num > max:
            max = num
        j -= 11
    i -= 1

print(max)