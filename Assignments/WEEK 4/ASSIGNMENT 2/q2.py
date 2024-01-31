"""
Write a Python program to generate a list of factorials less than 1000
using list comprehension.
Example output: [1, 2, 6, 24, 120, 720]
1000 can be changed to anything.

"""


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact


lst = [factorial(i) for i in range(1, 1000) if factorial(i) < 1000]

print(lst)
