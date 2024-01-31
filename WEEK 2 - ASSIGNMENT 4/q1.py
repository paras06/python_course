"""
Create a function named factorial which takes a integer as an input and returns the factorial of that number.

Factorial of 5 means 5 x 4 x 3 x 2 x 1 = 120
"""


def factorial(n):
    i = 1
    fact = 1
    while i <= n:
        fact = fact * i
        i += 1
    return fact


print(factorial(5))
